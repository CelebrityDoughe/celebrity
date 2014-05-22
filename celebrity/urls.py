# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^login/success/$',
        login_required(TemplateView.as_view(template_name='login_success.html'))),  # noqa

    url(r'^accounts/', include('userena.urls')),
    url(r'^davemour/', include(admin.site.urls)),

    url(r'', include('rating.urls', 'rating', 'rating')),
    url(r'', include('portals.urls', 'portals', 'portals')),
    url(r'', include('social_auth.urls')),
)
