# -*- coding: utf-8 -*-
from django import forms

from .models import SliderItem


class SliderItemForm(forms.ModelForm):

    class Meta:
        model = SliderItem
        exclude = ('slider', 'index', )
