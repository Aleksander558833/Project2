import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# redis-16054.c244.us-east-1-2.ec2.redns.redis-cloud.com:16054
# f5tZOyXLfFUWAImG7PCXw4T2nNHoj39L