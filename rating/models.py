# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from .constants import(
    ACTOR, MUSICIAN, TV, RADIO, POLITICIAN, ATHLETE
)


class Celebrity(models.Model):
    """
    Celebrity Model
    """
    CELEBRITY_CHOICES = (
        (ACTOR, 'Actors'),
        (MUSICIAN, 'Musicians'),
        (TV, 'TV'),
        (RADIO, 'Radio'),
        (POLITICIAN, 'Politicians'),
        (ATHLETE, 'Athletes'),
    )

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True)
    specificity = models.CharField(max_length=16, db_index=True,
                                   choices=CELEBRITY_CHOICES)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to="images/celebritypics")
    average_rate = models.FloatField(default=0, db_index=True, null=True)
    rate_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    """
    Rating model
    """
    user_id = models.IntegerField(db_index=True, blank=True, null=True)
    celebrity = models.ForeignKey(Celebrity, related_name="rates")
    rate = models.SmallIntegerField(default=0)
    review = models.TextField()
    dt_updated = models.DateTimeField(auto_now=True)

    @property
    def user(self):
        return User.objects.get(id=self.user_id)

    def __unicode__(self):
        return "%s - %d" % (self.user.username, self.rate)

    class Meta:
        ordering  = ('-id',)
