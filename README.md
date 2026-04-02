# Finance Tracker Backend API

## Overview

The Finance Tracker Backend API is a FastAPI-based backend system designed to manage financial transactions such as income and expenses. It provides CRUD operations, filtering capabilities, analytics insights, and role-based access control.

This project demonstrates backend API development using FastAPI, SQLAlchemy, and SQLite with production deployment on Render.

---

## Live Deployment

Swagger Documentation:

https://finance-tracker-backend-f0ch.onrender.com/docs

GitHub Repository:

https://github.com/Pranjalmishr1/finance-tracker-backend

---

## Features

### Transaction Management

* Create transaction
* View transactions
* Update transaction
* Delete transaction

### Filtering Support

Filter transactions by:

* Type (income / expense)
* Category
* Date

### Analytics Endpoints

Provides financial insights including:

* Total income
* Total expense
* Current balance
* Category-wise breakdown
* Monthly summary
* Recent activity

### Role-Based Access Control

Supports three user roles:

Viewer:

* Can view transactions only

Analyst:

* Can view transactions
* Can filter transactions
* Can access analytics endpoints

Admin:

* Full access
* Create transactions
* Update transactions
* Delete transactions

---

## Tech Stack

Framework:
FastAPI

Database:
SQLite

ORM:
SQLAlchemy

Server:
Uvicorn

Language:
Python

Deployment:
Render

---

## Project Structure

finance-tracker-backend/

app/

database.py

models.py

schemas.py

crud.py

main.py

routes/

transactions.py

analytics.py

users.py

utils/

permissions.py

requirements.txt

.gitignore

README.md

---

## Installation (Run Locally)

Clone the repository:

git clone https://github.com/Pranjalmishr1/finance-tracker-backend.git

Navigate to project folder:

cd finance-tracker-backend

Create virtual environment:

python -m venv venv

Activate virtual environment (Windows):

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn app.main:app --reload

Open Swagger documentation:

http://127.0.0.1:8000/docs

---

## API Endpoints

### Transactions

POST /transactions

Create transaction (Admin only)

GET /transactions

View all transactions

GET /transactions/{transaction_id}

View specific transaction

PUT /transactions/{transaction_id}

Update transaction (Admin only)

DELETE /transactions/{transaction_id}

Delete transaction (Admin only)

GET /transactions/filter-transactions

Filter transactions

---

### Analytics

GET /analytics/income

Returns total income

GET /analytics/expense

Returns total expense

GET /analytics/balance

Returns current balance

GET /analytics/category-breakdown

Returns category-wise summary

GET /analytics/monthly-summary

Returns monthly financial summary

GET /analytics/recent-activity

Returns recent transactions

---

## Role Usage Example

Example:

Create transaction as Admin:

POST /transactions?role=admin

View transactions as Viewer:

GET /transactions?role=viewer

Access analytics as Analyst:

GET /analytics/income?role=analyst

---

## Database

Database used:

SQLite

Database file:

finance.db

Automatically created on first run.

---

## API Documentation

Interactive Swagger UI available at:

https://finance-tracker-backend-f0ch.onrender.com/docs

---

## Deployment

Backend deployed using Render cloud platform.

Production URL:

https://finance-tracker-backend-f0ch.onrender.com

---

## Assignment Coverage

This backend fulfills the following requirements:

Transaction CRUD operations

Filtering functionality

Analytics endpoints

Role-based access control

SQLite database integration

Swagger documentation

Cloud deployment

Clean project structure

GitHub repository submission

---

## Future Improvements (Optional Enhancements)

JWT authentication support

PostgreSQL integration

Docker containerization

User authentication system

Environment configuration support

---

## Author

Pranjal Mishra

GitHub:

https://github.com/Pranjalmishr1
