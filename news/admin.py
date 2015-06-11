# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import NewsWebsite, Article


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'text', 'article_image'),
        }),
        ('Scraper', {
            'fields': ('image', 'news_website', 'url', 'checker_runtime'),
            'description': "If the following fields is not empty, the news was added by scrapper"
        }),
    )


admin.site.register(NewsWebsite)
admin.site.register(Article, ArticleAdmin)
