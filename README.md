# Smart Student Support System

## Overview

The Smart Student Support System is a web application designed to help students receive personalized academic support. It analyzes student performance, attendance and learning interests, then provides useful recommendations using machine learning. The system also offers dashboards for both students and administrators to track progress and manage academic activities more efficiently.


## Screenshot



<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/9727b32a-82b3-46ea-8941-2276c130cebf" />


<img width="1920" height="1080" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/3ef72485-2259-4926-8616-ce7179405e73" />


<img width="1920" height="1080" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/beb0beb0-eaeb-4ea8-a239-fc121be3a7ee" />


<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/23631310-63bb-47f8-9f2f-41399a7f9736" />


# Features

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


## Getting Started

Follow these steps to run the Smart Student Support System on your local machine.

1.**Clone or Download the Project**

git clone https://github.com/Sanjay9923/Smart-Student-Support-System.git
cd "Smart Student Support System"

2.**Install Required Dependencies**

This project uses Flask. Install it using:

pip install flask

If your project connects to MySQL, install:

pip install mysql-connector-python

If it uses SQLite, no extra installation is needed.

3.**Configure the Database**

Make sure your database is created and includes tables for:

Students

Login credentials

Attendance or performance (optional)

If you already have a .db file or MySQL connection inside app.py, no extra setup is required.

4.**Run the Application**

Start the Flask server:

python app.py

If everything loads correctly, you will see:

Running on http://127.0.0.1:5000/

5.**Open the Web Application**

Open your browser and visit:

http://127.0.0.1:5000/

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


## Project Contributor

Sanjay.s — Developer and Project Lead

Contributions are welcome. Feel free to submit pull requests or propose enhancements to help improve the project.








