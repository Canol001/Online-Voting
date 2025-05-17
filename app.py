from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, emit
from werkzeug.utils import secure_filename
import os
import bcrypt
from models import db, User, Category, Aspirant, Vote
from database import init_db
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads/profile_pics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize database
init_db(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard' if current_user.role == 'admin' else 'voter_dashboard'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            login_user(user)
            return redirect(url_for('admin_dashboard' if user.role == 'admin' else 'voter_dashboard'))
        flash('Invalid email or password', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        national_id = request.form['national_id']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = User(full_name=full_name, email=email, national_id=national_id, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash('Email or National ID already exists', 'error')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('voter_dashboard'))
    categories = Category.query.all()
    return render_template('admin_dashboard.html', categories=categories)

@app.route('/admin/create_poll', methods=['GET', 'POST'])
@login_required
def create_poll():
    if current_user.role != 'admin':
        return redirect(url_for('voter_dashboard'))
    if request.method == 'POST':
        category_name = request.form['category_name']
        aspirants = request.form.getlist('aspirant_name')
        parties = request.form.getlist('political_party')
        files = request.files.getlist('profile_picture')
        
        category = Category(name=category_name)
        db.session.add(category)
        db.session.commit()
        
        for name, party, file in zip(aspirants, parties, files):
            if name and party:
                filename = None
                if file:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                aspirant = Aspirant(
                    full_name=name,
                    profile_picture=filename,
                    political_party=party,
                    category_id=category.id
                )
                db.session.add(aspirant)
        db.session.commit()
        flash('Poll created successfully!', 'success')
        return redirect(url_for('admin_dashboard'))
    return render_template('create_poll.html')

@app.route('/voter/dashboard')
@login_required
def voter_dashboard():
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    categories = Category.query.all()
    voted_categories = [vote.category_id for vote in current_user.votes]
    return render_template('voter_dashboard.html', categories=categories, voted_categories=voted_categories)

@app.route('/vote/<int:category_id>', methods=['GET', 'POST'])
@login_required
def vote(category_id):
    if current_user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    category = Category.query.get_or_404(category_id)
    if Vote.query.filter_by(user_id=current_user.id, category_id=category_id).first():
        flash('You have already voted in this category', 'error')
        return redirect(url_for('voter_dashboard'))
    aspirants = Aspirant.query.filter_by(category_id=category_id).all()
    if request.method == 'POST':
        aspirant_id = request.form['aspirant_id']
        vote = Vote(user_id=current_user.id, aspirant_id=aspirant_id, category_id=category_id)
        db.session.add(vote)
        db.session.commit()
        # Emit vote update to all clients
        results = get_results(category_id)
        socketio.emit('vote_update', {'category_id': category_id, 'results': results})
        return redirect(url_for('results', category_id=category_id))
    return render_template('vote.html', category=category, aspirants=aspirants)

@app.route('/results/<int:category_id>')
@login_required
def results(category_id):
    category = Category.query.get_or_404(category_id)
    results = get_results(category_id)
    return render_template('results.html', category=category, results=results)

def get_results(category_id):
    aspirants = Aspirant.query.filter_by(category_id=category_id).all()
    results = []
    for aspirant in aspirants:
        vote_count = Vote.query.filter_by(aspirant_id=aspirant.id).count()
        results.append({
            'name': aspirant.full_name,
            'party': aspirant.political_party,
            'votes': vote_count,
            'profile_picture': aspirant.profile_picture
        })
    return results

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    socketio.run(app, debug=True)