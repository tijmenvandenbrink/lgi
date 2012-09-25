# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Device.last_update_by_snmp'
        db.alter_column('ci_device', 'last_update_by_snmp', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Device.last_update_by_cli'
        db.alter_column('ci_device', 'last_update_by_cli', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Device.last_update_by_snmp'
        db.alter_column('ci_device', 'last_update_by_snmp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None))

        # Changing field 'Device.last_update_by_cli'
        db.alter_column('ci_device', 'last_update_by_cli', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None))

    models = {
        'ci.component': {
            'Meta': {'object_name': 'Component'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'component_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'connected_ports': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'controller_mem': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ci.Device']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'fru_line_card': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fru_packet_mem': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'fru_route_mem': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'l3_engine': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'l3_engine_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'n_of_ports': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'part': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realm': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'reserved_ports': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'shutdown_ports': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'tan': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'ci.device': {
            'Meta': {'object_name': 'Device'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'boot_image': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'chassis_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'configuration_memory_in_use': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'configuration_register': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'hardware_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hardware_version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'hw_model': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'blank': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {}),
            'last_update_by_cli': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_update_by_snmp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'memory': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'mgmt_ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'os_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'os_version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'processor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'realm': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rom_system_version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rom_version': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sysname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['ci']