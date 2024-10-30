import os

from django.core.management import execute_from_command_line

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    active_passcards = []
    passcards = Passcard.objects.all()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())
