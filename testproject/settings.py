import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, ".."))


MEDIA_ROOT = os.path.join(BASE_DIR, "testproject", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "testproject", "static")
SECRET_KEY = "testproject-secretkey"
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

LANGUAGE_CODE = "de"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

WSGI_APPLICATION = "testproject.wsgi.application"
ROOT_URLCONF = "testproject.urls"

STATIC_URL = "/static/"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]
STATICFILES_DIRS = [os.path.join(BASE_DIR, "admin_styles", "static_dev")]

INSTALLED_APPS = [
    "testproject.testapp",
    "admin_styles",
    "compressor",
    "easy_thumbnails",
    "filer",
    "testproject.apps.ProjectAdminConfig",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "testproject", "db.sqlite3"),
    }
}


# ============================================================================
# COMPRESSOR/LIBSASS settings
# ============================================================================

COMPRESS_STORAGE = "compressor.storage.GzipCompressorFileStorage"
COMPRESS_PRECOMPILERS = [
    ("text/x-scss", "django_libsass.SassCompiler"),
]
LIBSASS_SOURCE_COMMENTS = False
LIBSASS_OUTPUT_STYLE = "compressed"
