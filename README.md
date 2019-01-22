# [WIP] django-manage

`django-manage` is a new tool to manage the django application on the command line.

To start the Django application, we can use the `django-manage` tool from anywhere in the project directory instead of running the 'manage.py' file with 'python'.

# Install

```bash
$ pip install django-manage --user --upgrade
```

# Usage

Create a example django project.

```bash
        $ mkdir my-project
        $ cd my-project
        $ python3 -m venv .venv
        $ source .venv/bin/activate
(.venv) $ pip install django
(.venv) $ django-admin startproject mysite
(.venv) $ mkdir mysite/apps
(.venv) $ mkdir mysite/apps/customers
(.venv) $ django-admin startapp customers mysite/apps/customers
(.venv) $ tree
.
├── manage.py
└── mysite
    ├── apps
    │   └── customers
    │       ├── admin.py
    │       ├── apps.py
    │       ├── __init__.py
    │       ├── migrations
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── tests.py
    │       └── views.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

4 directories, 12 files
(.venv) $ cd mysite/apps/customers
(.venv) $ python3 ../../../manage.py runserver
...
(.venv) $ django-manage original runserver
...
```
