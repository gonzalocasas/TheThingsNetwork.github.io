"""
Django settings for ttn_org project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = os.environ


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k68wehezi=b_gn4%cco$1&rvpe^xyz$(3kzyrb_4&oau)vh)xh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(env.get('DEBUG', True))

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markwhat',
    'jsonify',
    'waliki',
    'waliki.git',
    'waliki.attachments',
    'waliki.pdf',
    'waliki.togetherjs',
    'rest_framework',
    'mail_templated',

    'ttn',
    'wiki',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'subdomains.middleware.SubdomainURLRoutingMiddleware',
)

ROOT_URLCONF = 'ttn_org.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ttn_org.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if all(env.get(key) for key in ['MYSQL_HOST', 'MYSQL_DB', 'MYSQL_USER', 'MYSQL_PASSWORD']):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': env.get('MYSQL_DB'),
            'USER': env.get('MYSQL_USER'),
            'PASSWORD': env.get('MYSQL_PASSWORD'),
            'HOST': env.get('MYSQL_HOST'),
            'PORT': '3306'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

EMAIL_HOST = env.get('EMAIL_HOST')
EMAIL_PORT = env.get('EMAIL_PORT')
EMAIL_USE_TLS = bool(env.get('EMAIL_USE_TLS', False))
EMAIL_USE_SSL = bool(env.get('EMAIL_USE_SSL', True))
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD')
EMAIL_FROM = env.get('EMAIL_FROM', EMAIL_HOST_USER)
EMAIL_ADMIN = env.get('EMAIL_ADMIN')

SLACK_TOKEN = env.get('SLACK_TOKEN', '')
SLACK_CHANNEL = env.get('SLACK_CHANNEL', 'general')

API_INFLUX_HOST = env.get('API_INFLUX_HOST', '')
API_INFLUX_PORT = env.get('API_INFLUX_PORT', '')
API_INFLUX_DB = env.get('API_INFLUX_DB', '')


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


WALIKI_DEFAULT_MARKUP = 'Markdown'


REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ],
        'PAGE_SIZE': 1,  # wrapper, pagination
}
