# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _

from guardian.shortcuts import assign
from userena.models import UserenaBaseProfile


class UserProfile(UserenaBaseProfile):
    """
    User Profile
    """
    user = models.OneToOneField(User, unique=True, verbose_name=_('user'),
                                related_name='my_profile')


def create_user_profile(sender, instance, created, *args, **kwargs):
    """
    Create related user profile object when new user is registered
    """
    if created:
        UserProfile(user=instance).save()
        assign('change_profile', instance, instance.get_profile())
        assign('change_user', instance, instance)

post_save.connect(create_user_profile, User)
