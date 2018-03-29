import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_api.settings')

app = Celery('stock_api')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'load-data-every-single-minute': {
        'task': 'stock.tasks.get_data',
        'schedule': crontab(hour=23),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}