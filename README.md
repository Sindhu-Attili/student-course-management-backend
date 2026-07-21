# 🎓 Student Course Management System - Backend

<p align="center">
  <h3 align="center">RESTful Backend for the Student Course Management System</h3>

  <p align="center">
    A secure and scalable backend built using <b>Django</b> and <b>Django REST Framework</b> with JWT Authentication for managing students, courses, assignments, payments, certificates, and dashboard analytics.
  </p>
</p>

---

# ✨ Features

- 🔐 JWT Authentication
- 🛡 Secure Protected APIs
- 📊 Dashboard Statistics API
- 📚 Course Management
- 📝 Assignment Management
- 💳 Payment Management
- 🏆 Certificate Management
- 🔍 Search APIs
- 📑 Sorting
- 📄 Pagination
- 🧩 RESTful API Design
- ⚡ Modular Architecture

---

# 🛠 Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- MySQL
- Simple JWT
- CORS Headers

---

# 📂 Project Structure

```text
Student Course Management System
│
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── permissions.py
│
├── student_course_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 📡 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/token/` | Login |
| POST | `/api/token/refresh/` | Refresh Access Token |

---

## Dashboard

| Method | Endpoint |
|---------|----------|
| GET | `/api/dashboard-stats/` |

---

## Courses

| Method | Endpoint |
|---------|----------|
| GET | `/api/courses/` |
| POST | `/api/courses/` |
| PUT | `/api/courses/{id}/` |
| DELETE | `/api/courses/{id}/` |

---

## Assignments

| Method | Endpoint |
|---------|----------|
| GET | `/api/assignments/` |
| POST | `/api/assignments/` |
| PUT | `/api/assignments/{id}/` |
| DELETE | `/api/assignments/{id}/` |

---

## Payments

| Method | Endpoint |
|---------|----------|
| GET | `/api/payments/` |
| POST | `/api/payments/` |
| PUT | `/api/payments/{id}/` |
| DELETE | `/api/payments/{id}/` |

---

## Certificates

| Method | Endpoint |
|---------|----------|
| GET | `/api/certificates/` |
| POST | `/api/certificates/` |
| PUT | `/api/certificates/{id}/` |
| DELETE | `/api/certificates/{id}/` |

---

# 🔐 Authentication

This project uses **JWT (JSON Web Token)** Authentication.

After successful login:

- Access Token is generated
- Refresh Token is generated
- Protected endpoints require:

```text
Authorization: Bearer <access_token>
```

---

# 🗄 Database

The backend uses **MySQL** as the primary database.

Main Models:

- Student
- Course
- Assignment
- Payment
- Certificate

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/Sindhu-Attili/Student-Course-Management-System.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

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

### Run Development Server

```bash
python manage.py runserver
```

---

# 📦 Project Modules

- Authentication
- Dashboard
- Courses
- Assignments
- Payments
- Certificates

---

# 🔮 Future Enhancements

- 👤 User Profile APIs
- 📤 File Upload APIs
- 📊 Analytics APIs
- 📈 Reports
- 🔔 Notification APIs
- 👥 Role-Based Access Control

---

# 👨‍💻 Author

**Satya Sindhu**

Python Full Stack Developer

GitHub: https://github.com/Sindhu-Attili

---

⭐ If you found this project useful, consider giving it a star.