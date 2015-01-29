# -*- coding: utf-8 -*-
from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField


class Contact(models.Model):
    """
    Contact Page Model
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    detail = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s(%s) - %s' % (self.name, self.email, self.dt_created)
