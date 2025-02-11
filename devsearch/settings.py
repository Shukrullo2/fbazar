"""
Django settings for devsearch project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os






# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^e9k4)^ix$_!4)i8o(ifq&suu+-hnhsk92eeo(t1=1or@6*q-@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects.apps.ProjectsConfig',
    'users.apps.UsersConfig',
    'jobs.apps.JobsConfig',
    'storages',
    'captcha',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",

]

CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1', 'https://freelance.wiut.uz']


ROOT_URLCONF = 'devsearch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'projects/templates/'),
            os.path.join(BASE_DIR, 'users/templates/'),
            os.path.join(BASE_DIR, 'jobs/templates/'),
        ],
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

WSGI_APPLICATION = 'devsearch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases




# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME':  'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '246Shukrullo',
#         'HOST': 'database-1.cla2g0smg5j2.eu-central-1.rds.amazonaws.com',
#         'PORT': '5432',

#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': BASE_DIR / 'db.sqlite3',    
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'ashukrullowork@gmail.com'
EMAIL_HOST_PASSWORD = 'wwkxgwnebwlxbtkg'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

PASSWORD_RESET_TIMEOUT = 14400


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_ROOT = os.path.join(BASE_DIR, "static/images")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# CAPTCHA_IMAGE_SIZE = (30, 10)  # Width, Height

# # Other optional configurations
# CAPTCHA_FONT_SIZE = 40
# CAPTCHA_LETTER_ROTATION = (-35, 35)
# CAPTCHA_BACKGROUND_COLOR = '#ffffff'
# CAPTCHA_FOREGROUND_COLOR = '#000000'
# CAPTCHA_NOISE_FUNCTIONS = (
#     'captcha.helpers.noise_arcs',
#     'captcha.helpers.noise_dots',
# )
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'  # Example: simple math challenge


# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
# AWS_S3_ACCESS_KEY_ID = 'AKIAZI2LFXLF2YEJWM5S'
# AWS_S3_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'fbazaraaa'
# AWS_S3_FILE_OVERWRITE = False
# AWS_QUERYSTRING_AUTH = False
