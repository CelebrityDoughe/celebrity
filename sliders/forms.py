# -*- coding: utf-8 -*-
from django import forms

from .models import SliderItem, SliderItemComment


class SliderItemForm(forms.ModelForm):

    class Meta:
        model = SliderItem
        exclude = ('slider', 'index', )


class SliderItemCommentCreateFrom(forms.ModelForm):

    class Meta:
        model = SliderItemComment
        fields = ('content',)
