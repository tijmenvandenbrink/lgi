# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Device'
        db.create_table('ci_device', (
            ('realm', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('first_seen', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('unique_id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, blank=True)),
            ('mgmt_ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('sysname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_update_by_cli', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_update_by_snmp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('chassis_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('hardware_version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('hardware_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('rom_version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('rom_system_version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('configuration_register', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('memory', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('configuration_memory_in_use', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('boot_image', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('processor', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('os_version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('hw_model', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('os_family', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('ci', ['Device'])

        # Adding model 'Component'
        db.create_table('ci_component', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('realm', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('first_seen', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_seen', self.gf('django.db.models.fields.DateTimeField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('device_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ci.Device'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('component_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('connected_ports', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('shutdown_ports', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('n_of_ports', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('part', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fru_line_card', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fru_route_mem', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fru_packet_mem', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('l3_engine_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('l3_engine', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('tan', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('controller_mem', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('reserved_ports', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal('ci', ['Component'])


    def backwards(self, orm):
        # Deleting model 'Device'
        db.delete_table('ci_device')

        # Deleting model 'Component'
        db.delete_table('ci_component')


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