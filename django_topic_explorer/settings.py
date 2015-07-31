"""
Django settings for django_topic_explorer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^_uj&#+hs!=q57!%!ao%t#e$^q@8qtxh$3ejf@uh4rnw#igqwu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'topic_explorer',
    'see_topic',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_topic_explorer.urls'

WSGI_APPLICATION = 'django_topic_explorer.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-ve'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
            os.path.join(BASE_DIR, '../topic_explorer/static'),
)

TEMPLATE_DIRS = (
            TEMPLATE_PATH,
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django_topic_explorer.context_processors.baseurl",
)

#url comun para el proyecto
URL_COMUN='http://localhost:8000/'
## TOPIC EXPLORER SETTINGS
#TOPIC_EXPLORER_PATH = '/home/jredondo/Proyectos/Analisis_del_Discurso/src/topic-explorer/'
TOPIC_EXPLORER_PATH = '/home/cenditel/Interpretacion/'
FILES_PATH = TOPIC_EXPLORER_PATH +'demo-data/corpus_propuestas/pp'
MODELS_PATH = TOPIC_EXPLORER_PATH + 'demo-data/corpus_propuestas/models/'
CORPUS_FILE = MODELS_PATH + 'pp-nltk-en-freq5.npz'
#CORPUS_FILE = MODELS_PATH + 'ap-nltk-en-freq5.npz'
MODEL_PATTERN = MODELS_PATH + 'pp-nltk-en-freq5-LDA-K{0}-document-200.npz'
#MODEL_PATTERN = MODELS_PATH + 'ap-nltk-en-freq5-LDA-K{0}-document-20.npz'
CONTEXT_TYPE = 'document'
TOPICS = '10, 20, 30, 40, 50, 60, 70'
#TOPICS = '10, 20, 30, 40, 50, 60, 70, 80, 90, 100'
#TOPICS = '10, 20, 30, 40, 50, 60'
CORPUS_NAME = 'Deafult'
ICONS = 'link'

CORPUS_LINK = None
TOPIC_RANGE = None
DOC_TITTLE_FORMAT = None
DOC_URL_FORMAT = None


