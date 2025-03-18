import os
from codegenproject.wsgi import application

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codegenproject.settings')
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:5000'])