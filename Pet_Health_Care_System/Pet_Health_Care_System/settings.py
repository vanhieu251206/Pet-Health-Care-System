import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-ri%o8nq8)3tmf*rt**+$b31g6(*99ivyn+tv1p^_s_#)@asjsx'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pets',
    'rest_framework',
    'customer',
    'staff',
    'doctor',
    'media',
    'QTV',
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

# URL configuration
ROOT_URLCONF = 'Pet_Health_Care_System.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,  # Phải bật để Django tìm các static files trong app
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


# WSGI application
WSGI_APPLICATION = 'Pet_Health_Care_System.wsgi.application'

AUTH_USER_MODEL = 'pets.CustomUser'

LOGOUT_REDIRECT_URL = 'pets:login_page'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME','DBase'),
        'USER': os.getenv('DB_USER','root'),
        'PASSWORD': os.getenv('DB_PASSWORD','petscare'),
        'HOST': os.getenv('DB_HOST','127.0.0.1'),
        'PORT': os.getenv('DB_PORT','3306'),
    }
}

# Authentication
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'  # Đường dẫn URL để truy cập tệp tĩnh
STATICFILES_DIRS = []  # Không sử dụng thư mục static ở gốc project

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Đường dẫn URL để truy cập các tệp media (ảnh, video, v.v.)
MEDIA_URL = '/media/'

# Thư mục thực tế trên server nơi các tệp media được lưu
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'pets/static')]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
