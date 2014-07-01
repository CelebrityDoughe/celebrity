# -*- coding: utf-8 -*-
from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact Us Form
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'detail']


class AdvertiseForm(forms.Form):
    """
    Form for advertise
    """
    email = forms.EmailField()
    detail = forms.CharField()
