# -*- coding: utf-8 -*-
import random
import string

from django.contrib.auth.hashers import UNUSABLE_PASSWORD
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _

from guardian.shortcuts import assign_perm
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
        assign_perm('change_profile', instance, instance.get_profile())
        assign_perm('change_user', instance, instance)

        # set random password for the social auth users
        # Or it will be "!" by default.
        # The user with password "!" can not reset password(limited by Django)
        if instance.password == UNUSABLE_PASSWORD:
            random_pwd = ''.join([random.choice(string.letters) for i in range(8)])  # noqa
            instance.set_password(random_pwd)
            instance.save()

post_save.connect(create_user_profile, User)
