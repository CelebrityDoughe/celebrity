# -*- coding: utf-8 -*-
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


class Slider(models.Model):
    """
    Model for slider
    """
    name = models.CharField(u'Slider Name', max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)


class SliderItem(models.Model):
    """
    Item for slider
    """
    slider = models.ForeignKey(Slider)
    image = ThumbnailerImageField(upload_to='sliders')
    description = models.TextField(blank=True, null=True)
    index = models.IntegerField(db_index=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
