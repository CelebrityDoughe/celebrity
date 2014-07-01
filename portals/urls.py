# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ContactUsView, FlatPageView, IndexView, AdvertiseView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact-us/$', ContactUsView.as_view(), name='contact'),
    url(r'^advertise/$', AdvertiseView.as_view(), name='advertise'),
    url(r'^(?P<slug>\w+)/$', FlatPageView.as_view(), name='flat_page'),
)
