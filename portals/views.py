# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm


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
    success_url = reverse_lazy('portals', kwargs={'slug': 'thanks'})

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)
