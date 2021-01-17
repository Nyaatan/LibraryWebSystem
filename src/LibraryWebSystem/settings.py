import os
import mimetypes
import configparser

from pathlib import Path

db_conf_reader = configparser.ConfigParser()
db_conf_reader.read('../config.ini')
db_conf_data = db_conf_reader["database"]

BASE_DIR = Path(__file__).resolve().parent.parent
BOOKS_DIR = os.path.join(os.path.dirname(BASE_DIR), "books")

SECRET_KEY = 'x&3moqjm-%uq94cj3inhuhcn)r4tn$h#5p@)(tbmp!@@bjwmw5'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'LibraryApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryWebSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'LibraryApp.context_proc.check_if_logged_in'
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryWebSystem.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_conf_data["database"],
        'USER': db_conf_data["user"],
        'PASSWORD': db_conf_data["password"],
        'HOST': 'localhost',
        'PORT': db_conf_data["port"]
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

mimetypes.add_type('image/svg+xml', '.svg', True)
mimetypes.add_type("image/svg+xml", ".svgz", True)
