import os
from corsheaders.defaults import default_headers

main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "ab123@"
DEBUG = True

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    "idempotency-key",
]

INSTALLED_APPS = [
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "apps.merchant",
    "apps.ledger",
    "apps.payouts",
    "apps.idempotency",
    "corsheaders",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ]
}

ROOT_URLCONF = "config.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "playtopay",
        "USER": "postgres",
        "PASSWORD": "Sourav7452",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]

STATIC_URL = "/static/"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
