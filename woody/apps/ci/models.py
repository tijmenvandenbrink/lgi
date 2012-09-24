from datetime import datetime

from django.db import models

class CiCommonInfo(models.Model):
	realm = models.CharField(max_length=255, help_text="Please specify the realm this device belongs to")
	vendor = models.CharField(max_length=255, blank=True)
	timestamp = models.DateTimeField()
	active = models.BooleanField()

	class Meta:
		abstract = True

class Device(CiCommonInfo):
	unique_id = models.CharField(max_length=255, primary_key=True)
	device_id = models.CharField(max_length=255)
	hostname = models.CharField(max_length=255)
	ip_address = models.GenericIPAddressField(blank=True)
	mgmt_ip_address = models.GenericIPAddressField()
	sysname = models.CharField(max_length=255)
	description = models.CharField(max_length=255, blank=True)
	contact = models.CharField(max_length=255, blank=True)
	location = models.CharField(max_length=255, blank=True)

	source = models.CharField(max_length=255, blank=True)

	last_update_by_cli = models.DateTimeField(blank=True)
	last_update_by_snmp = models.DateTimeField(blank=True)
	
	chassis_type = models.CharField(max_length=255, blank=True)
	hardware_version = models.CharField(max_length=255, blank=True)
	hardware_id = models.CharField(max_length=255, blank=True)
	rom_version = models.CharField(max_length=255, blank=True)
	rom_system_version = models.CharField(max_length=255, blank=True)
	configuration_register = models.CharField(max_length=255, blank=True)
	memory = models.CharField(max_length=255, blank=True)
	configuration_memory_in_use = models.CharField(max_length=255, blank=True)
	boot_image = models.CharField(max_length=255, blank=True)
	processor = models.CharField(max_length=255, blank=True)
	os_version = models.CharField(max_length=255, blank=True)
	hw_model = models.CharField(max_length=255, blank=True)
	os_family = models.CharField(max_length=255, blank=True)

	def __unicode__(self):
		return self.device_id

class Component(CiCommonInfo):
	device_id = models.ForeignKey(Device, blank=True, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=255, 
							help_text="Please specify the name of the component")
	component_id = models.CharField(max_length=255, blank=True)
	connected_ports = models.PositiveIntegerField(blank=True)
	shutdown_ports = models.PositiveIntegerField(blank=True)
	n_of_ports = models.PositiveIntegerField(blank=True)
	part = models.CharField(max_length=255, blank=True)
	serial = models.CharField(max_length=255, blank=True)
	fru_line_card = models.CharField(max_length=255, blank=True)
	fru_route_mem = models.CharField(max_length=255, blank=True)
	fru_packet_mem = models.CharField(max_length=255, blank=True)
	l3_engine_type = models.CharField(max_length=255, blank=True)
	l3_engine = models.CharField(max_length=255, blank=True)
	tan = models.CharField(max_length=255, blank=True)
	description = models.CharField(max_length=255, blank=True)
	controller_mem = models.CharField(max_length=255, blank=True)
	reserved_ports = models.PositiveIntegerField(blank=True)
	cost = models.CharField(max_length=255, blank=True)
	version = models.CharField(max_length=255, blank=True)

	def __unicode__(self):
		return u"%s-%s" % (self.device_id, self.name)