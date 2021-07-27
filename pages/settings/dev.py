from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

CELERY_BROKER_URL = "redis://192.168.50.182:36379/0"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True
