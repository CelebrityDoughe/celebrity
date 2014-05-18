# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import CategoryView, CelebrityDetailView, SearchView


urlpatterns = patterns(
    '',
    url(r'^category/(?P<slug>\w+)/$',
        CategoryView.as_view(), name="category_list"),
    url(r'^celebrity/(?P<slug>[-_\w]+)/$',
        CelebrityDetailView.as_view(), name='celebrity_detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
)
