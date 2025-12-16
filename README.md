Student Management System (Django)

A portfolio-ready Django Student Management System that supports full CRUD (Create, Read, Update, Delete) operations for student records with a clean Bootstrap-style dashboard UI.

Features

Add new students

View students list in a table (dashboard style)

Update student details

Delete with confirmation page

SQLite database (default Django setup)

Clean UI using Django templates

Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap-style templates

Database: SQLite3

Project Structure

student_management/ # Django project (settings, urls)
students/ # Main app (models, views, forms, urls)
templates/students/ # HTML templates (UI)
manage.py # Django entry point

Getting Started (Local Setup)
1) Clone the repository

git clone https://github.com/
<your-username>/student-management-system-django.git
cd student-management-system-django

2) Create & activate virtual environment

Mac/Linux
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
venv\Scripts\activate

3) Install dependencies

If you have requirements.txt:
pip install -r requirements.txt

If you don't have requirements.txt, install Django:
pip install django

4) Run migrations

python manage.py migrate

5) Start the server

python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

Admin Panel (Optional)

Create an admin user:
python manage.py createsuperuser

Then open:
http://127.0.0.1:8000/admin/

Screenshots

Add screenshots for a stronger portfolio look.

Suggested structure:

docs/screenshots/dashboard.png

docs/screenshots/form.png

Recommended .gitignore

Make sure these are ignored:
venv/
pycache/
*.pyc
db.sqlite3
.env

Future Improvements (Roadmap)

Search & filter on student list

Pagination

Authentication (login/logout)

Export to CSV/PDF

Deploy on Render / PythonAnywhere

License

This project is open-source and available under the MIT License.

Author

Arafath-Abir
If you like this project, feel free to ⭐ star the repository.
