# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Test'
        db.create_table(u'objects_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field1', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'objects', ['Test'])


    def backwards(self, orm):
        # Deleting model 'Test'
        db.delete_table(u'objects_test')


    models = {
        u'objects.test': {
            'Meta': {'object_name': 'Test'},
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['objects']