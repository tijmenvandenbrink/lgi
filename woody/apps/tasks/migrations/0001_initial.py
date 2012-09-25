# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('tasks_profile', (
            ('unique_id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('realm', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('first_seen', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tasks', ['Profile'])

        # Adding model 'Task'
        db.create_table('tasks_task', (
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Profile'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('tasks', ['Task'])

        # Adding model 'Metric'
        db.create_table('tasks_metric', (
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
            ('metric', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('tasks', ['Metric'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('tasks_profile')

        # Deleting model 'Task'
        db.delete_table('tasks_task')

        # Deleting model 'Metric'
        db.delete_table('tasks_metric')


    models = {
        'tasks.metric': {
            'Meta': {'object_name': 'Metric'},
            'metric': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Task']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'tasks.profile': {
            'Meta': {'object_name': 'Profile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'realm': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Profile']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        }
    }

    complete_apps = ['tasks']