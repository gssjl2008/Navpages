CELERY_BROKER_URL = "redis://redis.public-service:6379/0"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pages',
        'USER': 'root',
        'PASSWORD': 'mysqlNb6f',
        'HOST': 'mysql-0.mysql-headness.public-service',
        'PORT': '3306',
    }
}

DEBUG = False
