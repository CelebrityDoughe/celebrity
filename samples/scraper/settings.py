# -*- coding: utf-8 -*-
import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celebrity.settings')

BOT_NAME = 'samples'

SPIDER_MODULES = ['dynamic_scraper.spiders', 'samples.scraper',]

USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [
    'dynamic_scraper.pipelines.ValidationPipeline',
    'samples.scraper.pipelines.DjangoWriterPipeline',
]
