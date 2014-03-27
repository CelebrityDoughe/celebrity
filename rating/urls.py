from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from rating.views import CategoryView, CelebrityDetailView, ContactUsView, SearchView


urlpatterns = patterns(
    '',
    url(r'^category/(?P<slug>\w+)/$', CategoryView.as_view(), name="category_list"),
    url(r'^celebrity/(?P<slug>[-_\w]+)/$', CelebrityDetailView.as_view(), name='celebrity_detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),

    #flat pages
    url(r'^terms-of-service/$', TemplateView.as_view(template_name="terms.html"), name="terms"),
    url(r'^contact-us/$', ContactUsView.as_view(), name="contact"),
    url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html"), name="thanks"),
)