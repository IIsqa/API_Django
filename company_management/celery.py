import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company_management.settings')

app = Celery('company_management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()