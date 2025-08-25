from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurant_management_project.settings")

app = Celery("restaurant_management_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Schedule task at 11:59 PM daily
app.conf.beat_schedule = {
    "generate-sales-report": {
        "task": "orders.tasks.generate_sales_report",
        "schedule": crontab(hour=23, minute=59),
    }
}
