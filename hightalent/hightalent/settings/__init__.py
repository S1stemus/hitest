from split_settings.tools import include

settings = [
    "django.py",
    "db_settings.py",
    "drf.py",
]

include(*settings)