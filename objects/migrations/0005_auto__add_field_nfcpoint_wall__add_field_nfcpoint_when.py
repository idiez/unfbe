# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NFCPoint.wall'
        db.add_column(u'objects_nfcpoint', 'wall',
                      self.gf('django.db.models.fields.CharField')(default='0x00', max_length=50),
                      keep_default=False)

        # Adding field 'NFCPoint.when'
        db.add_column(u'objects_nfcpoint', 'when',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 8, 2, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NFCPoint.wall'
        db.delete_column(u'objects_nfcpoint', 'wall')

        # Deleting field 'NFCPoint.when'
        db.delete_column(u'objects_nfcpoint', 'when')


    models = {
        u'objects.contactrelationship': {
            'Meta': {'unique_together': "(('from_contact', 'to_contact'),)", 'object_name': 'ContactRelationship'},
            'from_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_contacts'", 'to': u"orm['objects.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_contacts'", 'to': u"orm['objects.UserInfo']"})
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
        }
    }

    complete_apps = ['objects']