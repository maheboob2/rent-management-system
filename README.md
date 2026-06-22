# Rent Management System

A web-based Rent Management System built using Django that helps landlords and property managers efficiently manage tenants, rent payments, and property-related records.

## Overview

Managing rental properties manually can be time-consuming and error-prone. This application provides a centralized platform for storing tenant information, tracking rent payments, and managing rental records in an organized manner.

## Features

* Add, update, and delete tenant records
* Store tenant contact information
* Track rent payment history
* View all tenants in a structured dashboard
* Manage payment status and due dates
* Search and organize tenant data
* User-friendly interface built with HTML and CSS

## Technologies Used

* Python
* Django
* SQLite
* HTML
* CSS
* Git & GitHub

## Project Structure

```text
Rent Management System
│
├── tracker/
├── templates/
├── static/
├── migrations/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/maheboob2/rent-management-system.git
cd rent-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Open in Browser

```text
http://127.0.0.1:8000/
```

## Learning Outcomes

Through this project, I gained practical experience with:

* Django Models
* Django Views and Templates
* CRUD Operations
* Database Design
* Form Handling
* Static Files Management
* Git and GitHub Workflow

## Future Improvements

* Authentication and Authorization
* Email Notifications for Due Rent
* PDF Receipt Generation
* Monthly Rent Reports
* Advanced Search and Filtering
* Property Management Module

## Author

Maheboob Mulla

GitHub: https://github.com/maheboob2
