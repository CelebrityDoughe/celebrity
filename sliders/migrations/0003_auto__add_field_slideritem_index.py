# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SliderItem.index'
        db.add_column(u'sliders_slideritem', 'index',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SliderItem.index'
        db.delete_column(u'sliders_slideritem', 'index')


    models = {
        u'sliders.slider': {
            'Meta': {'object_name': 'Slider'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'sliders.slideritem': {
            'Meta': {'object_name': 'SliderItem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sliders.Slider']"})
        }
    }

    complete_apps = ['sliders']