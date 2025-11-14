# Smart Student Support System
## Overview

The Smart Student Support System is a web application designed to help students receive personalized academic support. It analyzes student performance, attendance and learning interests, then provides useful recommendations using machine learning. The system also offers dashboards for both students and administrators to track progress and manage academic activities more efficiently.


## Key Features

**Personalized Academic Analysis**: Analyzes performance, attendance and interests to understand each student's learning pattern.

**Machine Learning Recommendations**: Suggests suitable courses, study materials and improvement steps based on student data.

**Student Dashboard**: Gives students a clear view of their academic status, recommended actions and alerts.

**Admin Dashboard**: Allows administrators to monitor student performance, identify weak areas and send alerts.

**Automated Alerts**: Notifies students when performance drops or attendance becomes irregular.

**Secure User Authentication**: Login system for students and administrators with protected access.


## How It Works

1.**User Registration & Login**- Users create accounts and log in through the web interface.

2.**Data Collection**- Student academic data and attendance are stored in the MySQL database.

3.**Machine Learning Processing**- The system analyzes the data and generates personalized recommendations.

4.**Dashboards**- Students and admins can view performance trends, suggestions and alerts.

5.**Notifications**- In-app alerts are triggered when students need academic attention.

## Tech Stack

**Frontend**: HTML, CSS, JavaScript

**Backend**: Python 

**Database**: MySQL

**Machine Learning**: Scikit-learn, Pandas, NumPy

**Other Tools**: Flask-Login, dotenv


## Installation & Setup

Follow these steps to install and run the Smart Student Support System on your local machine.

1.**Clone the Repository**

git clone https://github.com/your-username/Smart-Student-Support-System.git
cd Smart-Student-Support-System

2.**Create and Activate a Virtual Environment**

It’s recommended to use a virtual environment.

Create environment

python -m venv venv


Activate environment

venv\Scripts\activate


 3.**Install Dependencies**

Install all necessary Python libraries using:

pip install -r requirements.txt

4.**Configure the MySQL Database**

Make sure MySQL server is installed and running.

Create the database

CREATE DATABASE student_support_db;


If your project includes initdb.py, run this to set up tables:

python initdb.py

6.**Train or Load the Machine Learning Model**

If you have a machine learning script like ml_model.py, run:

python ml_model.py


This will generate and save the model used by the system.

7.**Start the Flask Server**

Run the main application:

python app.py

8.**Open the Application**

Once the server is running, open your browser and go to:

http://127.0.0.1:5000/


## Project Structure

Smart Student Support System/

│
├── app.py                      # Main application file

│
├── database/                   # Database files

│   └── student_support.sql     # Database script or data file

│
├── templates/                  # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── chatbot.html
│   ├── dashboard.html

│
├── static/                     # CSS, JS, and images
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/



## System Architecture

User → Web Interface (Flask App)
↕
MySQL Database
↕
Flask Backend → Machine Learning Model → Recommendations & Alerts



## Future Improvements

Add a mobile app for students and faculty.

Integrate chatbot support for instant academic queries.

Implement real-time attendance analytics using IoT or RFID.

Add a detailed AI dashboard for student risk prediction.

Enable multilingual support for wider accessibility.


## Project Contributor

**Sanjay.s** — Developer and Project Lead

Contributions are welcome. Feel free to submit pull requests or propose enhancements to help improve the project.



## License

This project is open-source and available under the MIT License.




