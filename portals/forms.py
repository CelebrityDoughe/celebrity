# -*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    """
    Contact Us Form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'detail']
