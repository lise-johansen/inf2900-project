"""
Django settings for app_project project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add the directory containing Vue.js static files to STATICFILES_DIRS
STATICFILES_DIRS = [
    # Adjust the path as needed
    os.path.join(BASE_DIR, "../../Team11/vue-app/dist"),
]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&@nmsdwxy*o!l1_r8p@t#&w4n@w3ljbeoqzq4t87q8accy=fdw'

# Change the following to VUE app URL
# FRONTEND_URL = 'https://django.dybedahlserver.net'
FRONTEND_URL = 'localhost:8080/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Use HTTPS for secure connections
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['localhost:8080', '127.0.0.1', '129.151.210.152','django.dybedahlserver.net', 'localhost']

USER_MODEL = 'airfinn.User'
AUTH_USER_MODEL = 'airfinn.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'airfinn.apps.AirfinnConfig',
    'corsheaders',
    # Django SSL extension
    'django_extensions',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Other middleware classes...

]

CORS_ALLOWED_ORIGINS = ['https://django.dybedahlserver.net', 'https://rentopia.dybedahlserver.net', 'http://localhost:8080', 'http://localhost:8000']
CORS_ALLOW_ALL_ORIGINS = True # CORS middleware
CORS_ALLOW_CREDENTIALS = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SIMPLE_JWT = {
    # Example: Refresh token expires after 1 day
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    'ROTATE_REFRESH_TOKENS': True,
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

AUTHENTICATION_BACKENDS = [
    # Default Django authentication backend
    'django.contrib.auth.backends.ModelBackend',
    # Add any additional authentication backends as needed
]

ROOT_URLCONF = 'app_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'app_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'postgres',
    #     'USER': 'postgres',
    #     'PASSWORD': 'St3rkP@ss0rd',
    #     'HOST': '129.151.210.152',
    #     'PORT': '5432',
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'postgres',
    #     'USER': 'postgres',
    #     'PASSWORD': 'St3rkP@ss0rd',
    #     'HOST': '129.151.210.152',
    #     'PORT': '5432',
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '../db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/https://localhost:8000/api/dashboard/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email server for SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zeptomail.eu'  # Your Zoho Mail SMTP server address
EMAIL_PORT = 465  # Zoho Mail SMTP port for SSL
EMAIL_USE_SSL = True  # Use SSL/TLS for secure connection
EMAIL_USE_TLS = False  # No need for TLS if using SSL
EMAIL_HOST_USER = 'emailapikey'  # Your Zoho Mail API key as the username
# Your Zoho Mail Send Mail Token 1 as the password
EMAIL_HOST_PASSWORD = 'yA6KbHsMugT+kDpWQ0hs1ZWNoo40qqAwjXm+sX/kdJYuKNnn26E71BJkdNTvJzWLitfX56oDbY5AL4C9vYoLfJZiZ9YEL5TGTuv4P2uV48xh8ciEYNYkgZigCrAVFa9MeBoiDSw2QfgoWA=='
DEFAULT_FROM_EMAIL = 'dybedahlserver.net'  # Your domain/sender address 