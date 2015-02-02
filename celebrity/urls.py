# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from sliders.views import SliderDetailView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^login/success/$',
        login_required(TemplateView.as_view(template_name='login_success.html'))),  # noqa

    url(r'^accounts/', include('userena.urls')),
    url(r'^slider/(?P<pk>\d+)/$', SliderDetailView.as_view(), name='public_slider'),
    url(r'^davemour/sliders/', include('sliders.urls', 'sliders', 'sliders')),
    url(r'^davemour/', include(admin.site.urls)),

    url(r'', include('rating.urls', 'rating', 'rating')),
    url(r'', include('portals.urls', 'portals', 'portals')),
    url(r'', include('social_auth.urls')),
)
