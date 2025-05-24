# 🗳️ ElectraVote - Secure Online Voting System

**ElectraVote** is a modern, secure, and user-friendly online voting web application that empowers voters to cast ballots effortlessly from anywhere. Built with Flask and styled with Tailwind CSS, ElectraVote provides a seamless experience for both voters and administrators.

---

## 🌐 Tech Stack

| Layer                 | Technology                     |
| --------------------- | ------------------------------ |
| **Frontend**          | HTML, Tailwind CSS, JavaScript |
| **Backend**           | Python, Flask                  |
| **Real-Time Updates** | Flask-SocketIO                 |
| **Database**          | SQLite (default) / PostgreSQL  |
| **Icons & UI**        | Custom emojis, SVGs            |
| **Authentication**    | Flask-Login                    |
| **Package Manager**   | pip                            |

---

## 🌟 Features

* ✅ **Secure Voting**: Ensures voter authentication and data integrity.
* 💡 **User-Friendly Interface**: A flat, minimalistic design with a teal, white, and orange color scheme for a clean and intuitive user experience.
* 📊 **Real-Time Results**: Displays election results with animated progress bars that visually indicate leading candidates (orange for leaders, teal for others) using Socket.IO for live updates.
* 📱 **Responsive Design**: Fully responsive layout for mobile and desktop users, powered by Tailwind CSS.
* 🔐 **Admin Capabilities**:

  * Create polls with dynamic aspirant addition, including category selection and profile picture uploads.
  * View existing categories with aspirant counts and total votes in the admin dashboard.
* 🧑‍💻 **Voter Dashboard**: Allows voters to see available polls, vote, and view results for completed polls.
* 📤 **Dynamic Forms**: Supports drag-and-drop profile picture uploads for aspirants during poll creation.
* ✍️ **Custom Icons**: Uses unique icons like `✍️` for creating polls and `📈` for viewing results in the admin dashboard.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

* 🐍 **Python 3.8+**
* 📦 **pip** (Python package manager)
* 🧲 **Virtualenv** (optional but recommended)
* 🔌 **Node.js** (for Socket.IO client)
* 🌐 A modern web browser (e.g., Chrome, Firefox)

---

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Canol001/Online-Voting.git
   cd Online-Voting
   ```

2. **Create Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate     # On Linux/Mac
   venv\Scripts\activate        # On Windows
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:

   ```bash
   flask run
   ```

---

## 🔐 Default Login Credentials

### Admin:

* **Email**: `admin@voting.com`
* **Password**: `admin123`

> ⚠️ **Note**: Change the admin password in production for security.

### Voter:

Register a new voter account via the `/register` page with:

* Full name
* Email address
* National ID number
* Password

Then log in with your registered email and password.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 🚀 Live Demo

*https://electravote-4dki.onrender.com/login*

---
![image](https://github.com/user-attachments/assets/51b0a4a9-511f-4505-a55d-2627e99bac2a)

## Login and navigate the system

This project is open-source and available under the [MIT License](LICENSE).

---

![image](https://github.com/user-attachments/assets/a8a5ea8d-fe68-45ef-813b-b8b91d8b85e7)

