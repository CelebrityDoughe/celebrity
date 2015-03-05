# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Rating', fields ['dt_updated']
        db.create_index(u'rating_rating', ['dt_updated'])


    def backwards(self, orm):
        # Removing index on 'Rating', fields ['dt_updated']
        db.delete_index(u'rating_rating', ['dt_updated'])


    models = {
        u'rating.celebrity': {
            'Meta': {'object_name': 'Celebrity'},
            'average_rate': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'rate_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'specificity': ('django.db.models.fields.CharField', [], {'max_length': '16', 'db_index': 'True'})
        },
        u'rating.rating': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Rating'},
            'celebrity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rates'", 'to': u"orm['rating.Celebrity']"}),
            'dt_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'review': ('django.db.models.fields.TextField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rating']