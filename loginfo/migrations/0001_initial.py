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

        # Adding model 'LogModel'
        db.create_table('loginfo_logmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('model_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('id_obj', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('loginfo', ['LogModel'])


    def backwards(self, orm):
        
        # Deleting model 'LogRequest'
        db.delete_table('loginfo_logrequest')

        # Deleting model 'LogModel'
        db.delete_table('loginfo_logmodel')


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
            'user_info': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['loginfo']
