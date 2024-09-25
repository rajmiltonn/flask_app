# Steptech Assignment - Flask API Project.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup Instructions](#setup-instructions)
3. [Project Structure](#project-structure)
4. [Database Schema](#database-schema)
5. [SQL Queries](#sql-queries)
6. [Author](#author)


----

## Introduction

This project is a Flask API application developed as part of the Steptech Assignment for assessing skills in Python Flask, MySQL database interaction, and Git version control..

---

## Setup Instructions

### Prerequisites

- Python 3.x installed on your machine.
- MySQL database server installed locally..

### Steps to Set Up the Project

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd steptech_assignment

2. **Install Flask and MySQL Connector:**

   ```bash
   pip install flask flask-mysqldb

3. **Database Setup:**
  * Ensure MySQL server is running.
  * Create a new database named users:
    
    ```bash
    pip install flask flask-mysqldb and USE users;

4. **Import Database Schema:**
Use the following SQL schema to create the users table:

    ```bash
    CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role VARCHAR(50));

5. **Run the Flask Application:**

   ```bash
   python app.py
   
  * This will start the development server at http://127.0.0.1:5000/.
***Project Structure***
The project structure is organized as follows:

    ```bash
      flask_project/
      │
      ├── app/  # Directory containing application-specific modules and packages.
      ├── static/  # Directory for static assets like CSS and JavaScript files.
      │   ├── css/
      │   │   └── style.css  # CSS file for styling the application.
      │   └── js/
      │       └── script.js  # JavaScript file for client-side scripting.
      └── templates/  # Directory for HTML templates used in the application.
          ├── new_user.html  # Template for adding a new user.
          ├── users.html  # Template for displaying a list of users.
          └── user_detail.html  # Template for displaying details of a user.
      ├── config.py  # Configuration file for the Flask application.
      ├── db.py  # File containing database-related functionality.
      ├── requirements.txt  # File listing Python dependencies required for the project.
      └── test_mysql_connection.py  # Script to test MySQL database connection.
      └── app.py  # Main Flask application file.  

5. **Author:**
Raj Milton
Contact: rajmilton55555@gmail.com
