from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from rating.views import CategoryView, CelebrityDetailView


urlpatterns = patterns(
    '',
    url(r'^category/(?P<slug>\w+)/$', CategoryView.as_view(), name="category_list"),
    url(r'^celebrity/(?P<slug>[-_\w]+)/$', CelebrityDetailView.as_view(), name='celebrity_detail'),
)