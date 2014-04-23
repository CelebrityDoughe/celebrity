# -*- coding: utf-8 -*-
from celery.task import task
from dynamic_scraper.utils.task_utils import TaskUtils

from .models import NewsWebsite


@task()
def run_spiders():
    t = TaskUtils()
    t.run_spiders(NewsWebsite, 'scraper', 'scraper_runtime', 'article_spider')
