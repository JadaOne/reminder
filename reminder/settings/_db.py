from env_utils import get_bool, get_env, get_int  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env('DB_NAME', 'reminder'),
        'USER': get_env('DB_USER','reminder'),
        'PASSWORD': get_env('DB_PASS', 'reminder'),
        'HOST': get_env('DB_HOST','127.0.0.1'),
        'PORT': get_env('DB_PORT', '5432'),
    }
}
