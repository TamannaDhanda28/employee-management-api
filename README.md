# Employee Management REST API

A simple **Employee Management System** built using **FastAPI**.
This project provides a RESTful API to manage employee data including creating, reading, updating, and deleting employee records.

The project also includes **JWT Authentication**, **Swagger API documentation**, and a **SQLite database** for storing employee data.

## 🚀 Features

* Create new employees
* View employee list
* Update employee information
* Delete employee records
* Token-based authentication
* Swagger interactive API documentation
* FastAPI backend with SQLite database

## 🛠 Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Uvicorn
* HTML / JavaScript (Frontend)

# ⚙️ How to Run This Project

Follow these steps to run the project on your system.

## 1️⃣ Clone the Repository

git clone https://github.com/TamannaDhanda28/employee-management-api.git

Go inside the project folder:

cd employee-management-api

## 2️⃣ Create Virtual Environment

python -m venv venv

Activate the environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

## 3️⃣ Install Dependencies

pip install -r requirements.txt

## 4️⃣ Run the Backend Server

python -m uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000

## 5️⃣ Open API Documentation (Swagger)

Open this in your browser:

http://127.0.0.1:8000/docs

Swagger UI allows you to test all API endpoints interactively.


# 🔑 Authentication

To access protected endpoints:

1. Use the login API
2. Generate a **JWT token**
3. Add the token in Swagger Authorize section

Example:

Bearer YOUR_TOKEN

# 📌 API Endpoints

### Authentication

POST /token

Generate access token.


### Employees

Create Employee

POST /api/employees/

Get Employees

GET /api/employees/

Get Employee by ID

GET /api/employees/{id}

Update Employee

PUT /api/employees/{id}

Delete Employee

DELETE /api/employees/{id}

# 🧪 Testing

Tests are available in the `tests` folder.

Run tests using:

pytest

# 👩‍💻 Author

Tamanna Dhanda

GitHub:
https://github.com/TamannaDhanda28


# ⭐ Project Purpose

This project was built for learning and demonstrating:

* REST API development
* FastAPI framework
* Authentication using JWT
* CRUD operations
* Backend and frontend integration
