===> Create Project: Initialize a new Django project named django_todo.

django-admin startproject django_todo
cd django_todo
===============================================================================================> 
Create Application: Create a new app called todo.

python manage.py startapp todo_app
===============================================================================================> 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo_app',
]

===> we have to add the django app i.e todo_app to the INSTALLED_APPS in settings.py file in project_module folder : 

======================================================================================================>
note : manually we have to create the databae 
but : based on model the tables and their columns schema is created in the given database 
===> Configure the Database  : 
    Database Settings: In settings.py, configure the database to use PostgreSQL. 
    
    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'form_details_django_db',
        'USER': 'postgres',
        'PASSWORD': 'Anil12345',
        'HOST': 'localhost',  # Use 'localhost' for local setup
        'PORT': '5432',  # Default PostgreSQL port
    }
}

======================================================================================================> 
===> signal for success of migrations  : 

rgukt@lenovo-e41-55:~/Desktop/WT/telusko/django_todo$ python3 manage.py makemigrations
No changes detected
rgukt@lenovo-e41-55:~/Desktop/WT/telusko/django_todo$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, todo_app
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying todo_app.0001_initial... OK

