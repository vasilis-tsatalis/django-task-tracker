# django-task-tracker
Python Django framework for task list management

# Start the Web Server 
$ python manage.py runserver

# Stes to create project

$ python -m venv venv
$ venv\Scripts\activate.bat
$ pip install django
$ python -m pip freeze > requirements.txt
$ django-admin startproject todo_project .
$ django-admin startapp todo_app
$ python manage.py runserver
$ python manage.py makemigrations todo_app
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver

# Build Docker Image
$ docker build -t django-task-tracker .

