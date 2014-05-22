# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm
from news.models import Article, NewsWebsite


class IndexView(TemplateView):
    """
    Home page
    """
    template_name = 'portals/index.html'

    def get_context_data(self, **kwargs):
        """
        Add news to the context
        """
        data = super(IndexView, self).get_context_data(**kwargs)
        # get the latest article from all the websites
        articles = []
        for website in NewsWebsite.objects.all():
            atcs = Article.objects.filter(news_website=website).order_by('-id')  # noqa
            if atcs:
                articles.append(atcs[0])
        data.update({'articles': articles})
        return data


class FlatPageView(TemplateView):
    """
    Template View for flat page only
    """
    def get_template_names(self):
        return ['portals/%s.html'%self.kwargs['slug']]


class ContactUsView(FormView):
    """
    Contact Us page
    """

    template_name = 'portals/contact-us.html'
    form_class = ContactForm
    success_url = reverse_lazy('portals:flat_page', kwargs={'slug': 'thanks'})

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)
