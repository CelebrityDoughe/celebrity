# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import NewsWebsite, Article


admin.site.register(NewsWebsite)
admin.site.register(Article)
