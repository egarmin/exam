# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'LogRequest.priority'
        db.add_column('loginfo_logrequest', 'priority', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'LogRequest.priority'
        db.delete_column('loginfo_logrequest', 'priority')


    models = {
        'loginfo.logmodel': {
            'Meta': {'object_name': 'LogModel'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_obj': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'loginfo.logrequest': {
            'Meta': {'object_name': 'LogRequest'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user_info': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['loginfo']
