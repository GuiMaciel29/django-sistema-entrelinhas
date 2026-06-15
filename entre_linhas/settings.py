from pathlib import Path

# ==================================================
# BASE
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# SEGURANÇA
# ==================================================

SECRET_KEY = 'django-insecure-_=e5abhzc6pv7ea4zjuuccj&iv+7jv%*#%an3o8=$09w@p@6!='

DEBUG = False

ALLOWED_HOSTS = [
    'GuilhermeMarinho.pythonanywhere.com',
]

# ==================================================
# APLICAÇÕES
# ==================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]

# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==================================================
# URLS
# ==================================================

ROOT_URLCONF = 'entre_linhas.urls'

# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ==================================================
# WSGI
# ==================================================

WSGI_APPLICATION = 'entre_linhas.wsgi.application'

# ==================================================
# BANCO DE DADOS
# ==================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==================================================
# SENHAS
# ==================================================

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

# ==================================================
# INTERNACIONALIZAÇÃO
# ==================================================

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_TZ = True

# ==================================================
# ARQUIVOS ESTÁTICOS
# ==================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'core' / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# ==================================================
# MEDIA
# ==================================================

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ==================================================
# LOGIN
# ==================================================

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/login/'

# ==================================================
# DEFAULT PK
# ==================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'