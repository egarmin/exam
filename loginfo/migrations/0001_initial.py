# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LogRequest'
        db.create_table('loginfo_logrequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('path', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('user_info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('loginfo', ['LogRequest'])


    def backwards(self, orm):
        
        # Deleting model 'LogRequest'
        db.delete_table('loginfo_logrequest')


    models = {
        'loginfo.logrequest': {
            'Meta': {'object_name': 'LogRequest'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'user_info': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['loginfo']
