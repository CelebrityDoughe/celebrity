# -*- coding: utf-8 -*-
import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celebrity.settings')

BOT_NAME = 'news'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'news.scraper',]

USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'news.scraper.pipelines.DjangoWriterPipeline',
]
