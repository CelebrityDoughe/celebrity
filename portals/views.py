# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import DetailView

from .forms import ContactForm, AdvertiseForm
from news.models import Article, NewsWebsite


class IndexView(TemplateView):
    """
    Home page
    """
    template_name = 'portals/index.html'
    news_on_page = 10

    def _get_website_news(self, num=10):
        '''
        Get the latest article from all the websites

        :param num: int - how much articles you need
        :return: list - list of articles
        '''
        articles = []

        for website in NewsWebsite.objects.all():
            atcs = Article.objects.filter(news_website=website).order_by('-id')  # noqa

            if atcs:
                articles.append(atcs[0])

            if len(articles) == num:
                return articles

        return articles

    def get_context_data(self, **kwargs):
        """
        Add news to the context
        """
        data = super(IndexView, self).get_context_data(**kwargs)

        articles = Article.objects.filter(news_website__isnull=True).order_by('-id')[:self.news_on_page]

        if len(articles) < self.news_on_page:
            difference = self.news_on_page - len(articles)

            articles = list(articles) + self._get_website_news(difference)

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
        contact = form.save()

        # send email to celebdbag@gmail.com
        send_mail(
            u'Contact from %s' % contact.name,
            u'Contact Email: %s\nContent: %s' % (contact.email, contact.detail),
            'admin@celebritydbag.com',
            ['celebdbag@gmail.com'],
            fail_silently=True)

        return super(ContactUsView, self).form_valid(form)


class AdvertiseView(FormView):
    """
    View for advertise
    """
    form_class = AdvertiseForm
    template_name = 'portals/advertise.html'
    success_url = reverse_lazy('portals:flat_page', kwargs={'slug': 'thanks'})

    def form_valid(self, form):
        """
        Send email notification to admin
        """
        data = form.cleaned_data

        # send email to celebdbag@gmail.com
        send_mail(
            u'Advertise from %s' % data['email'],
            u'Advertise Email: %s\nContent: %s' % (data['email'], data['detail']),
            'admin@celebritydbag.com',
            ['celebdbag@gmail.com'],
            fail_silently=True)

        return super(AdvertiseView, self).form_valid(form)


class NewsDetail(DetailView):
    model = Article
    template_name = 'portals/news_detail.html'
    context_object_name = "news_item"

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        articles = Article.objects.filter(news_website__isnull=True).exclude(
            id=self.object.id).order_by('-id')[:10]

        context.update({'articles': articles})
        return context
