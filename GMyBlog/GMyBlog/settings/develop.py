from .base import *  # NOQA

DATABASES = {
     'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'MYBLOG_DB',
            'USER': 'root',
            'PASSWORD': '1338.332',
            'HOST': 'localhost',
            'PORT': 3306,
            'CONN_MAX_AGE': 10 * 60,
            'OPTIONS': {'charset': 'utf8mb4'},
        },
}

DEBUG = True
