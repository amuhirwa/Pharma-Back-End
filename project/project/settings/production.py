# -*- coding: utf-8 -*-
from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "my_testdatabase",
        "USER": "my_testdatabase_user",
        "PASSWORD": "ogQSffCkoF4kDoBIzVKI4MCTJtmj1l07",
        "HOST": "dpg-d21ve8e3jp1c738c2rv0-a.oregon-postgres.render.com",
        "PORT": "5432",                    # default Postgres port
        "TEST": {
            "NAME": "my_testdatabase",
        },
        "ATOMIC_REQUESTS": True,
    }
}
