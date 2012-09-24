import os
import csv
import pdb
from datetime import datetime

from optparse import make_option

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from apps.ci.models import CiCommonInfo, Device

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
			make_option('--import',
				action='store',
				dest='importfile',
				default=False,
				help='Bulk import devices from .csv file'),
				)
	args = '''<realm>'''
	help = 'Bulk adds devices from a file'

	def handle(self, *args, **options):
		csvheader = ['device_id', 'vendor', 'ip_address', 'source', 'sysname', 
					'description', 'contact', 'location', 'last_update_by_cli', 
					'chassis_type', 'hardware_version', 'hardware_id', 'rom_version', 
					'rom_system_version', 'configuration_register', 'memory', 
					'memory', 'configuration_memory_in_use', 'boot_image', 
					'processor', 'os_version', 'mgmt_ip_address', 'hw_model', 'os_family', 
					'last_update_by_snmp', 'hostname']

		realm = args[0]

		if os.path.exists(options['importfile']):
			csvfile = csv.DictReader(open(options['importfile'], 'rb'), fieldnames=csvheader, delimiter=',')
			for dev in csvfile:
				unique_id = '%s-%s' % (realm, dev['device_id'])
				try:
					d = Device.objects.get(pk=unique_id)
					self.stdout.write('Device already exists "%s"\n' % dev['device_id'])
				except Device.DoesNotExist:
					try:
						dev['last_update_by_snmp'] = datetime.strptime(dev['last_update_by_snmp'], '%m/%d/%y %H:%M:%S')
						dev['last_update_by_cli'] = datetime.strptime(dev['last_update_by_cli'], '%m/%d/%y %H:%M:%S')
					except:
						dev['last_update_by_cli'] = datetime.now()
						dev['last_update_by_snmp'] = datetime.now()

					d = Device(realm=realm, timestamp=timezone.now(), pk=unique_id, **dev)
					d.save()
					self.stdout.write('Successfully added device "%s"\n' % dev['device_id'])