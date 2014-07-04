# -*- coding: utf-8 -*-
class DBRouter(object):
    """
    A router to control all database operations on models in the
    rating application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to celebrity.
        """
        if model._meta.app_label == 'rating':
            return 'celebrity'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to celebrity.
        """
        if model._meta.app_label == 'rating':
            return 'celebrity'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == 'rating' or \
                obj2._meta.app_label == 'rating':
            return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the auth app only appears in the celebrity
        database.
        """
        if db == 'celebrity':
            return model._meta.app_label == 'rating'
        elif model._meta.app_label == 'rating':
            return False
        return None
