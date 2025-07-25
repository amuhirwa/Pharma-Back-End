# -*- coding: utf-8 -*-
from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DATABASE_NAME", "pharcy"),
        "USER": config("DATABASE_USER", "my_testdatabase_user"),
        "PASSWORD": config("DATABASE_PASSWORD", "ogQSffCkoF4kDoBIzVKI4MCTJtmj1l07"),
        "HOST": config("DATABASE_HOST", "dpg-d21ve8e3jp1c738c2rv0-a"),
        "PORT": config("PORT",default="5432"),
        "TEST": {
            "NAME": "my_testdatabase",
        },
       "ATOMIC_REQUESTS": True

    }
}
