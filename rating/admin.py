# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Celebrity, Rating


admin.site.register(Celebrity)
admin.site.register(Rating)
