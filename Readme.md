# ElectraVote - Secure Online Voting System

**ElectraVote** is a modern, secure, and user-friendly online voting web application that empowers voters to cast ballots effortlessly from anywhere. Built with Flask and styled with Tailwind CSS, ElectraVote provides a seamless experience for both voters and administrators.

## ✨ Features

* **Secure Voting**: Ensures voter authentication and data integrity.
* **User-Friendly Interface**: A flat, minimalistic design with a teal, white, and orange color scheme for a clean and intuitive user experience.
* **Real-Time Results**: Displays election results with animated progress bars that visually indicate leading candidates (orange for leaders, teal for others) using Socket.IO for live updates.
* **Responsive Design**: Fully responsive layout for mobile and desktop users, powered by Tailwind CSS.
* **Admin Capabilities**:

  * Create polls with dynamic aspirant addition, including category selection and profile picture uploads.
  * View existing categories with aspirant counts and total votes in the admin dashboard.
* **Voter Dashboard**: Allows voters to see available polls, vote, and view results for completed polls.
* **Dynamic Forms**: Supports drag-and-drop profile picture uploads for aspirants during poll creation.
* **Custom Icons**: Uses unique icons like ✍️ for creating polls and 📈 for viewing results in the admin dashboard.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* **pip** (Python package manager)
* **Virtualenv** (optional but recommended)
* **Node.js** (for Socket.IO client)
* A modern web browser (e.g., Chrome, Firefox)

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/electravote.git
   cd electravote
   ```

## 👤 Default Login Credentials

**Admin:**

* Email: `admin@voting.com`
* Password: `admin123`

> **Note**: Change the admin password in production for security.

**Voter:**

* Register a new voter account via the `/register` page with:

  * Full name
  * Email address
  * National ID number
  * Password
* Log in with the registered email and password.

[canolowana6@gmail.com](mailto:canolowana6@gmail.com)\\
