To create django project
# linux command
django-admin startproject velocity

# windows command
django-admin.exe startproject velocity
project structure
mini_django_v1 (project-directory)

    - README.md
    - requirements.txt
    - venv
    - velocity  (project-root)
        - manage.py
        - velocity  (project-settings)
            - __init__.py
            - asgi.py
            - wsgi.py
            - settings.py
            - urls.py
        - blog (application)
            - __init__.py
            - admin.py
            - apps.py
            - models.py
            - tests.py
            - views.py
            - migrations   (results after running `makemigrate` command.)
                - __init__.py
Django architecture
django follows MVT architecture

models.py :: To write data-models
view.py :: To write business logic
tests.py :: To write unit-test
admin.py :: For admin interface
django files
manage.py :: this script helps us with management of site. It helps us to to start web server.

settings.py :: contains configuration for the website

urls.py :: this is a file for URL management

wsgi.py :: deployment purpose

asgi.py :: deployment purpose

default database with django
sqlite
when we do python manage.py migrate we basically create all the tables in listed in all the applications
how to create tables associated with sub-applications?
Django has pre-built sub-applications available in itself.
We can create database tables using those apps by using following command
cd <project-directory>   # cd velocity
python manage.py migrate
To run the application
python manage.py runserver
Synopsis to start with django

Step 1: create directory mkdir <project-root>
Step 2: cd to directory in step 1
Step 3: django-admin.exe startproject velocity
Step 4: cd velocity
Step 5: create DB tables python manage.py migrate
Step 6: run project python manage.py runserver
Step 7: create app => python manage.py startapp blog
Step 8: Inform django we have created new app by appending app name to the INSTALLED_APPS list in settings.py
Step 9: Let django know that we have created new model python manage.py makemigrations blog
Step 10: migrate DB python manage.py migrate
Step 11: Register newly created model on admin interface using admin.py
Step 12: Create user and password using python manage.py createsuperuser
Step 13: Run application python manage.py runserver and check admin interface by heading to /admin
Thumb rule for project root directory
In terms of django, wherever your manage.py file exists, that directory is called as working directory of project (aka project root).