# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Person'
        db.create_table('personal_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('personal', ['Person'])

        # Adding model 'Contacts'
        db.create_table('personal_contacts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='contacts', to=orm['personal.Person'])),
            ('jid', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=55, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('appendix', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('personal', ['Contacts'])


    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('personal_person')

        # Deleting model 'Contacts'
        db.delete_table('personal_contacts')


    models = {
        'personal.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'appendix': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jid': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'contacts'", 'to': "orm['personal.Person']"}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '55', 'blank': 'True'})
        },
        'personal.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['personal']
