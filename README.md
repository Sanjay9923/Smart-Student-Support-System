# Smart-Student-Support-System

## Overview

The Smart Student Support System is a web application designed to help students receive personalized academic support. It analyzes student performance, attendance and learning interests, then provides useful recommendations using machine learning. The system also offers dashboards for both students and administrators to track progress and manage academic activities more efficiently.


## Preview (Screenshot)

### Home Page

![Screenshot (1)](https://github.com/user-attachments/assets/3d283a1c-1d16-4f6c-9728-73a40d55b851)

### Register Page

![Screenshot (2)](https://github.com/user-attachments/assets/5398ef13-f9ea-46ad-b3fe-95d77265c0d4)

### Login Page

![Screenshot (3)](https://github.com/user-attachments/assets/b42d6b33-2162-452f-8d31-64c2848ff10f)

### Student Chatbot Page

![Screenshot (4)](https://github.com/user-attachments/assets/29d135ef-74cd-4f81-ba9e-8a34094f964e)
![Screenshot (5)](https://github.com/user-attachments/assets/d4a64922-96af-47df-ae29-3ba9a423a0c8)


## Features

- **Personalized Academic Analysis**: Analyzes performance, attendance and interests to understand each student's learning pattern.

- **Machine Learning Recommendations**: Suggests suitable courses, study materials and improvement steps based on student data.

- **Student Dashboard**: Gives students a clear view of their academic status, recommended actions and alerts.

- **Admin Dashboard**: Allows administrators to monitor student performance, identify weak areas and send alerts.

- **Automated Alerts**: Notifies students when performance drops or attendance becomes irregular.

- **Secure User Authentication**: Login system for students and administrators with protected access.


## How It Works

1.**User Registration & Login**- Users create accounts and log in through the web interface.

2.**Data Collection**- Student academic data and attendance are stored in the MySQL database.

3.**Machine Learning Processing**- The system analyzes the data and generates personalized recommendations.

4.**Dashboards**- Students and admins can view performance trends, suggestions and alerts.

5.**Notifications**- In-app alerts are triggered when students need academic attention.


## Project Structure

```bash
Student-Support-System/
│
├── app.py
├── database.db
│
└── templates/
    ├── login.html
    ├── index.html
    ├── chatbot.html
    └── register.html
```


## Getting Started

Follow these steps to run the Smart Student Support System on your local machine.

1.**Clone or Download the Project**
```bash
git clone https://github.com/Sanjay9923/Smart-Student-Support-System.git
cd "Smart Student Support System"
```

2.**Install Required Dependencies**

This project uses Flask. Install it using:
```bash
pip install flask
```

If your project connects to MySQL, install:
```bash
pip install mysql-connector-python
```

If it uses SQLite, no extra installation is needed.

3.**Configure the Database**

Make sure your database is created and includes tables for:

Students

Login credentials

Attendance or performance (optional)

If you already have a .db file or MySQL connection inside app.py, no extra setup is required.

4.**Run the Application**

Start the Flask server:
```bash
python app.py
```

If everything loads correctly, you will see:

```bash
Running on http://127.0.0.1:5000/
```

5.**Open the Web Application**

Open your browser and visit:

```bash
http://127.0.0.1:5000/
```

You will see the login page.

6.**Demo Login Credentials (For Testing)**

Student Login

Username: student01

Password: student123

Admin Login

Username: admin

Password: admin123


## Technologies Used

**Frontend**: HTML, CSS, JavaScript

**Backend**: Python (Flask Framework)

**Database**: MySQL or SQLite (depending on your setup)

**Libraries / Tools**: Flask, MySQL Connector / sqlite3, Jinja2 Templates


## Future Improvements

Add a mobile app for students and faculty.

Integrate chatbot support for instant academic queries.

Implement real-time attendance analytics using IoT or RFID.

Add a detailed AI dashboard for student risk prediction.

Enable multilingual support for wider accessibility.


## Author

Sanjay.s — Developer and Project Lead

Contributions are welcome. Feel free to submit pull requests or suggest improvements.


## License

This project is **free to use** and does not contains any license.






