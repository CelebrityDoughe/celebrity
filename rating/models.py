# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Celebrity(models.Model):
    """
    Celebrity Model
    """
    CELEBRITY_CHOICES = (
        ('A', 'Actors'),
        ('M', 'Musicians'),
        ('T', 'TV'),
        ('R', 'Radio'),
        ('S', 'Sports'),
        ('P', 'Politicians')
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    specificity = models.CharField(max_length=1, choices=CELEBRITY_CHOICES)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to="images/celebritypics")

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    """
    Rating model
    """
    user = models.ForeignKey(User)
    celebrity = models.ForeignKey(Celebrity, related_name="rates")
    rate = models.SmallIntegerField(default=0)
    review = models.TextField()
    dt_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %d" % (self.user.username, self.rate)
