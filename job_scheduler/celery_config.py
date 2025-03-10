from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_scheduler.settings')

app = Celery('JobScheduler')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    worker_concurrency=3,
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
