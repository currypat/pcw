# patcurryworks.com/main/settings/production.py
"""
Django production settings.
"""

from main.settings.base import *
DEBUG = False

ALLOWED_HOSTS = ["https://patcurryworks.com",
                 "https://www.patcurryworks.com",
                 "http://patcurryworks.com",
                 "http://www.patcurryworks.com"
]

if "RDS_HOSTNAME" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ["RDS_DB_NAME"],
            "USER": os.environ["RDS_USERNAME"],
            "PASSWORD": os.environ["RDS_PASSWORD"],
            "HOST": os.environ["RDS_HOSTNAME"],
            "PORT": os.environ["RDS_PORT"],
        }
    }

# I am not sure how all this stuff works or why it is important
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
