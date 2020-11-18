import os 

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '6(rzqzvsz!6zzaigu9%tiqj*x-ym8^$3cs+z89hb0-0hsyux&o'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '567306842155-aufnact8cp02qfrtejs766m3p4ubgb9p.apps.googleusercontent.com' # Google Consumer Key

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'OuzCRAWBweaJneakqho2eAa2' # Google Consumer Secret