# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Task', fields ['uuid']
        db.delete_unique('tasks_task', ['uuid'])

        # Adding field 'Task.id'
        db.add_column('tasks_task', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=0 ,primary_key=True),
                      keep_default=False)


        # Changing field 'Task.uuid'
        db.alter_column('tasks_task', 'uuid', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Deleting field 'Task.id'
        db.delete_column('tasks_task', 'id')


        # Changing field 'Task.uuid'
        db.alter_column('tasks_task', 'uuid', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True))
        # Adding unique constraint on 'Task', fields ['uuid']
        db.create_unique('tasks_task', ['uuid'])


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'polling_server': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasks.Profile']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['tasks']
