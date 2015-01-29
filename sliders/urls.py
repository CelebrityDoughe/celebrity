# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import(
    SliderCreateView, SliderListView, SliderItemListView, SliderItemCreateView,
    SliderItemUpdateView, SliderItemDeleteView, SliderDeleteView
)


urlpatterns = patterns(
    '',
    url(r'^$', SliderListView.as_view(), name='list'),
    url(r'^create/$', SliderCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', SliderDeleteView.as_view(), name='delete'),
    url(r'^(?P<slider_pk>\d+)/items/$', SliderItemListView.as_view(), name='items'),
    url(r'^(?P<slider_pk>\d+)/items/create/$', SliderItemCreateView.as_view(), name='create_item'),
    url(r'^(?P<slider_pk>\d+)/items/(?P<pk>\d+)/update/$', SliderItemUpdateView.as_view(), name='update_item'),
    url(r'^(?P<slider_pk>\d+)/items/(?P<pk>\d+)/delete/$', SliderItemDeleteView.as_view(), name='delete_item'),
)
