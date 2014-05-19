# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import ContactUsView, FlatPageView


urlpatterns = patterns(
    '',
    url(r'^contact-us/$', ContactUsView.as_view(), name="contact"),
    url(r'^(?P<slug>\w+)/$', FlatPageView.as_view(), name='flat_page'),
)
