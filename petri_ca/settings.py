"""
Django settings for petri_ca project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import dj_database_url
import os


import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR , "petri_ca",".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.environ.get('DEBUG')) == "True"
PASSWORD = (os.environ.get('PASSWORD'))
FRONTEND_LINK = "https://petrichor.events/"
BACKEND_LINK = "https://petrichor-backend.vercel.app/"
if DEBUG:
    FRONTEND_LINK = "http://localhost:5173"
    BACKEND_LINK = "https://petrichor-backend.vercel.app/"
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

if  DEBUG:
    CSRF_TRUSTED_ORIGINS = [
        'https://petrichor.events', 'https://petrichor-events.vercel.app', 'https://x.petrichor.events',"https://finance-petrichor.vercel.app","https://petrichor-backend.vercel.app",
    ]
    ALLOWED_HOSTS = [
        'https://petrichor.events', 'https://petrichor-events.vercel.app', 'x.petrichor.events',"petrichor-backend.vercel.app", "petri-back.vercel.app","https://finance-petrichor.vercel.app","finance-petrichor.vercel.app"
    ]
    CORS_ORIGIN_WHITELIST = [
        'https://petrichor.events', 'https://petrichor-events.vercel.app', 'https://.petrichor.events',"https://finance-petrichor.vercel.app","https://petrichor-backend.vercel.app", 
    ]

else:


    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:5173', 'https://petrichor.events', 'https://petrichor-events.vercel.app', 'https://x.petrichor.events'
    ]
    ALLOWED_HOSTS = [
        'localhost','127.0.0.1', 'https://petrichor.events', 'https://petrichor-events.vercel.app', ".vercel.app", 'x.petrichor.events'
    ]
    CORS_ORIGIN_WHITELIST = [
        'http://localhost:5173', 'https://petrichor.events', 'https://petrichor-events.vercel.app', 'https://.petrichor.events'
    ]


SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # or 'django.contrib.sessions.backends.cache'
SESSION_COOKIE_SECURE = not DEBUG  # Set to True if using HTTPS

FORGET_SALT_KEY = os.environ.get("FORGET_SALT_KEY")
FORGET_KEY = os.environ.get("FORGET_KEY")
FORGET_TOKEN_MAX_AGE = timedelta(minutes=5)

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app',
    'internal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'custom.middleware.PetrichorAuthMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'petri_ca.urls'

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'custom.authorizor.PetrichorJWTAuthentication',
    ],
}

SIMPLE_JWT = {
    # sets the lifetime of the access token generated on login
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5,days=30),
}

AUTHENTICATION_BACKENDS=[
    "django.contrib.auth.backends.ModelBackend"
]

WSGI_APPLICATION = 'petri_ca.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
if DEBUG:
    print("Using Local Database")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
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
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build' ,'static')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings for sending email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('MAIL_HOST')
EMAIL_HOST_PASSWORD = os.getenv('MAIL_PWD')
EMAIL_PORT = os.getenv('MAIL_PORT')
