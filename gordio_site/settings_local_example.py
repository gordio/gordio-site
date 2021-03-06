import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=3)r(3_75p10a%26n#&cs+utrs7kga#@0la)(=j5*tndzftz4&'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1', ]


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Sending emeails
# https://docs.djangoproject.com/en/dev/topics/email/
# Good for development debug
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
