import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.conf.update(
    broker_url="redis://127.0.0.1:6379/0",
    result_backend="redis://127.0.0.1:6379/0",
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
