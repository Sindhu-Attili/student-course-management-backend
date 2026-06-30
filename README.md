# 🎓 Student Course Management System - Backend

A robust RESTful backend built with **Django** and **Django REST Framework** for the Student Course Management System. It provides secure JWT authentication and REST APIs for managing students, courses, assignments, payments, and certificates.

---

## 🚀 Features

- 🔐 JWT Authentication
- 👨‍🎓 Student Management APIs
- 📚 Course Management APIs
- 📝 Assignment Management APIs
- 💳 Payment Management APIs
- 🏆 Certificate Management APIs
- 🔍 Search, Filtering & Ordering Support
- 📄 API Documentation with Swagger
- 🗄️ MySQL Database Integration
- ⚡ RESTful API Design

---

## 🛠️ Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- Simple JWT
- MySQL
- django-filter
- drf-spectacular

---

## 📂 Project Structure

```
Student-Course-Management-System/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── education/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── permissions.py
│   └── utils.py
│
├── manage.py
├── requirements.txt
└── db.sqlite3 / MySQL
```

---

## 🔄 Backend Request Flow

```
Client (React)
       │
       ▼
Axios Request
       │
       ▼
Django URL
       │
       ▼
ViewSet
       │
       ▼
Serializer
       │
       ▼
MySQL Database
       │
       ▼
JSON Response
       │
       ▼
React Frontend
```

---

## 📡 Available APIs

### Authentication

- POST `/api/token/`
- POST `/api/token/refresh/`

### Students

- GET `/api/students/`
- POST `/api/students/`
- PUT `/api/students/{id}/`
- DELETE `/api/students/{id}/`

### Courses

- GET `/api/courses/`
- POST `/api/courses/`
- PUT `/api/courses/{id}/`
- DELETE `/api/courses/{id}/`

### Assignments

- GET `/api/assignments/`
- POST `/api/assignments/`
- PUT `/api/assignments/{id}/`
- DELETE `/api/assignments/{id}/`

### Payments

- GET `/api/payments/`
- POST `/api/payments/`
- PUT `/api/payments/{id}/`
- DELETE `/api/payments/{id}/`

### Certificates

- GET `/api/certificates/`
- POST `/api/certificates/`
- PUT `/api/certificates/{id}/`
- DELETE `/api/certificates/{id}/`

---

## 🔐 Authentication

The API uses **JWT (JSON Web Token)** authentication.

Example Authorization Header:

```text
Authorization: Bearer <access_token>
```

---

## 📖 API Documentation

Swagger/OpenAPI documentation is available at:

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Sindhu-Attili/Student-Course-Management-System.git
```

### Navigate into the project

```bash
cd Student-Course-Management-System
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Start the Server

```bash
python manage.py runserver
```

The backend will start at:

```
http://127.0.0.1:8000/
```

---

## 🗄️ Database

This project uses **MySQL** as its primary database.

Database configuration is managed through:

```
config/settings.py
```

---

## 🔗 Frontend Repository

The frontend is built using React.js.

➡️ **Frontend Repository:**

https://github.com/Sindhu-Attili/Student-Course-Management-Frontend

---

## 📌 Project Status

🚧 **Currently Under Development**

Completed:

- JWT Authentication
- Student APIs
- Course APIs
- Assignment APIs
- Payment APIs
- Certificate APIs
- Search
- Filtering
- Ordering
- Swagger Documentation

Upcoming:

- Dashboard Statistics API
- Student Profile API
- Performance Improvements
- Deployment

---

## 👨‍💻 Author

**Sindhu Attili**

GitHub:
https://github.com/Sindhu-Attili

---

⭐ If you found this project useful, consider giving it a star!