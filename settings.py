import os
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY','dev-only-change-before-deployment')
DEBUG=os.environ.get('DJANGO_DEBUG','false').lower()=='true'
ALLOWED_HOSTS=[x.strip() for x in os.environ.get('DJANGO_ALLOWED_HOSTS','localhost,127.0.0.1').split(',') if x.strip()]
CSRF_TRUSTED_ORIGINS=[x.strip() for x in os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS','').split(',') if x.strip()]
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','core']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'core'/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='wsgi.application'
DATABASES={'default':{'ENGINE':'django.db.backends.postgresql','NAME':os.environ.get('POSTGRES_DB','investors'),'USER':os.environ.get('POSTGRES_USER','investors'),'PASSWORD':os.environ.get('POSTGRES_PASSWORD',''),'HOST':os.environ.get('POSTGRES_HOST','db'),'PORT':os.environ.get('POSTGRES_PORT','5432'),'CONN_MAX_AGE':60}}
AUTH_PASSWORD_VALIDATORS=[{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator','OPTIONS':{'min_length':12}},{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE='ar'; TIME_ZONE='Africa/Cairo'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; STATIC_ROOT=BASE_DIR/'staticfiles'; STORAGES={'staticfiles':{'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage'}}
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
LOGIN_URL='login'; LOGIN_REDIRECT_URL='dashboard'; LOGOUT_REDIRECT_URL='login'
SESSION_COOKIE_HTTPONLY=True; SESSION_COOKIE_SECURE=not DEBUG; CSRF_COOKIE_SECURE=not DEBUG; SECURE_SSL_REDIRECT=os.environ.get('SECURE_SSL_REDIRECT','true').lower()=='true' and not DEBUG
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDED_PROTO','https'); SECURE_HSTS_SECONDS=31536000 if not DEBUG else 0; SECURE_HSTS_INCLUDE_SUBDOMAINS=not DEBUG
SECURE_CONTENT_TYPE_NOSNIFF=True; X_FRAME_OPTIONS='DENY'; SESSION_COOKIE_SAMESITE='Lax'
