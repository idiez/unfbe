# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactRelationship'
        db.create_table(u'objects_contactrelationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_contacts', to=orm['objects.UserInfo'])),
            ('to_contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_contacts', to=orm['objects.UserInfo'])),
        ))
        db.send_create_signal(u'objects', ['ContactRelationship'])

        # Adding unique constraint on 'ContactRelationship', fields ['from_contact', 'to_contact']
        db.create_unique(u'objects_contactrelationship', ['from_contact_id', 'to_contact_id'])

        # Removing M2M table for field friends on 'UserInfo'
        db.delete_table(db.shorten_name(u'objects_userinfo_friends'))


    def backwards(self, orm):
        # Removing unique constraint on 'ContactRelationship', fields ['from_contact', 'to_contact']
        db.delete_unique(u'objects_contactrelationship', ['from_contact_id', 'to_contact_id'])

        # Deleting model 'ContactRelationship'
        db.delete_table(u'objects_contactrelationship')

        # Adding M2M table for field friends on 'UserInfo'
        m2m_table_name = db.shorten_name(u'objects_userinfo_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_userinfo', models.ForeignKey(orm[u'objects.userinfo'], null=False)),
            ('to_userinfo', models.ForeignKey(orm[u'objects.userinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_userinfo_id', 'to_userinfo_id'])


    models = {
        u'objects.contactrelationship': {
            'Meta': {'unique_together': "(('from_contact', 'to_contact'),)", 'object_name': 'ContactRelationship'},
            'from_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_contacts'", 'to': u"orm['objects.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_contacts'", 'to': u"orm['objects.UserInfo']"})
        },
        u'objects.nfcpoint': {
            'Meta': {'object_name': 'NFCPoint'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'belongsTo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['objects.UserInfo']"}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'posId': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'objects.test': {
            'Meta': {'object_name': 'Test'},
            'field1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'field2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'objects.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['objects.UserInfo']", 'null': 'True', 'through': u"orm['objects.ContactRelationship']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_pic_uri': ('django.db.models.fields.CharField', [], {'default': "'dummy_4'", 'max_length': '50'})
        }
    }

    complete_apps = ['objects']