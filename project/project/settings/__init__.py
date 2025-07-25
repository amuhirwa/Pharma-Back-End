# -*- coding: utf-8 -*-
from decouple import config

from .base import *

LOCAL = False


if LOCAL:
    print("LOCAL MODE")
    from .local import *
else:
    print("PRODUCTION MODE")
    from .production import *
