# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NFCPoint'
        db.create_table(u'objects_nfcpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('posId', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('registered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('belongsTo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['objects.UserInfo'])),
        ))
        db.send_create_signal(u'objects', ['NFCPoint'])

        # Adding model 'UserInfo'
        db.create_table(u'objects_userinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('user_pic_uri', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'objects', ['UserInfo'])

        # Adding M2M table for field friends on 'UserInfo'
        m2m_table_name = db.shorten_name(u'objects_userinfo_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_userinfo', models.ForeignKey(orm[u'objects.userinfo'], null=False)),
            ('to_userinfo', models.ForeignKey(orm[u'objects.userinfo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_userinfo_id', 'to_userinfo_id'])


    def backwards(self, orm):
        # Deleting model 'NFCPoint'
        db.delete_table(u'objects_nfcpoint')

        # Deleting model 'UserInfo'
        db.delete_table(u'objects_userinfo')

        # Removing M2M table for field friends on 'UserInfo'
        db.delete_table(db.shorten_name(u'objects_userinfo_friends'))


    models = {
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
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['objects.UserInfo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_pic_uri': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['objects']