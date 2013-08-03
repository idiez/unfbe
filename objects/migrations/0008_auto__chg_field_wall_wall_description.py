# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Wall.wall_description'
        db.alter_column(u'objects_wall', 'wall_description', self.gf('django.db.models.fields.CharField')(max_length=140))

    def backwards(self, orm):

        # Changing field 'Wall.wall_description'
        db.alter_column(u'objects_wall', 'wall_description', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'objects.contactrelationship': {
            'Meta': {'unique_together': "(('from_contact', 'to_contact'),)", 'object_name': 'ContactRelationship'},
            'from_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_contacts'", 'to': u"orm['objects.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_contacts'", 'to': u"orm['objects.UserInfo']"})
        },
        u'objects.entry': {
            'Meta': {'object_name': 'Entry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {}),
            'wall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['objects.Wall']"})
        },
        u'objects.fblink': {
            'Meta': {'object_name': 'Fblink'},
            'fb_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'objects.nfcpoint': {
            'Meta': {'object_name': 'NFCPoint'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'belongsTo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['objects.UserInfo']"}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'posId': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wall': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'when': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'objects.rating': {
            'Meta': {'object_name': 'Rating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'value': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'wall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['objects.Wall']"})
        },
        u'objects.test': {
            'Meta': {'object_name': 'Test'},
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'field2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'objects.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends+'", 'to': u"orm['objects.UserInfo']", 'through': u"orm['objects.ContactRelationship']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_pic_uri': ('django.db.models.fields.CharField', [], {'default': "'dummy_4'", 'max_length': '50'})
        },
        u'objects.wall': {
            'Meta': {'object_name': 'Wall'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'wall_description': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'wall_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'wall_last_seen': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'wall_pos_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'wall_title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['objects']