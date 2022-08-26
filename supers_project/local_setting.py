# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eohas5g5(&#3u0)rt85z23@75pncy0or_#$gexz%!*-t4uuip0'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supers_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}