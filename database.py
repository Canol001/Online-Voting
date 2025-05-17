from models import db, User
import bcrypt

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        # Create default admin if not exists
        admin = User.query.filter_by(email='admin@voting.com').first()
        if not admin:
            hashed_password = bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            admin = User(
                full_name='Admin User',
                email='admin@voting.com',
                national_id='ADMIN001',
                password=hashed_password,
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()