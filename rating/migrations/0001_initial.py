# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Celebrity'
        db.create_table(u'rating_celebrity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('specificity', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image1', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'rating', ['Celebrity'])


    def backwards(self, orm):
        # Deleting model 'Celebrity'
        db.delete_table(u'rating_celebrity')


    models = {
        u'rating.celebrity': {
            'Meta': {'object_name': 'Celebrity'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'specificity': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['rating']