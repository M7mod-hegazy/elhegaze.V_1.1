"""
Django settings for frist project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from django.contrib.messages import constants as messages
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '57Eb060Ef463C7E9396850Adc95D2Ec3115B68174D72C468'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '172.31.32.246',
    '172.31.43.167',
    'eb-env.eba-aapubfdx.us-west-2.elasticbeanstalk.com',
    'www.elhegazi.com',
    'elhegazi.com',
    '127.0.0.1'
    ]


# Application definition

INSTALLED_APPS = [
    'mypages.apps.MypagesConfig',
    'accounts.apps.AccountsConfig',
    'products.apps.ProductsConfig',
    'more.apps.MoreConfig',
    'orders.apps.OrdersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    "storages",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'frist.urls'


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

WSGI_APPLICATION = 'frist.wsgi.application'

STATICFILE_FINDERS = (
  'django_collectstatic_bower.staticfiles.finders.BowerComponentFinder',
)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'elhegazyDB',
        'USER': 'm7mod',
        'PASSWORD': '2351970321',
        'HOST': 'elhegazydb.c773b6wa4rxs.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR/'frist/static'

]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# media folder
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'



LOGOUT_REDIRECT_URL = 'index'
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'signin'

STATICFILE_FINDERS = (
    'django_collectstatic_bower.staticfiles.finders.BowerComponentFinder',
)




# Custom massages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'

}

AWS_ACCESS_KEY_ID = 'AKIATNUG7D6U3XZDCSXD'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'elhegazi'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'