import os
from pathlib import Path

# Корень проекта (папка dark_academia_project, где лежит manage.py)
BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'django-insecure-dark-academia-test-key'

# Для отладки оставляем True, но на живом сайте потом поменяешь на False
DEBUG = True

# Разрешаем все домены для Timeweb
ALLOWED_HOSTS = ['*']

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # твое приложение
]

# Middleware (Whitenoise СТРОГО на втором месте)
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

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Добавил на случай, если у тебя есть общая папка templates
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Отключаем валидаторы для тестов (чтобы не ругался на простые пароли)
AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- НАСТРОЙКИ СТАТИКИ (БЕЗ ПОВТОРОВ) ---
STATIC_URL = '/static/'
# Папка, где лежат файлы (CSS, картинки) прямо сейчас
STATICFILES_DIRS = [BASE_DIR / 'static']
# Папка, куда Django соберет всё для работы сайта (создастся сама)
STATIC_ROOT = BASE_DIR / 'staticfiles'
# Магия для работы статики на хостинге
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
