# Student Management System (Django)

A clean, portfolio-ready **Django CRUD** app to manage student records with a simple **dashboard UI**.

## Features
- Create, view, update, delete students
- Bootstrap-style templates
- SQLite database

## Tech
**Django • Python • HTML/CSS • SQLite**

## Run Locally
```bash
git clone https://github.com/<your-username>/student-management-system-django.git
cd student-management-system-django

python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
