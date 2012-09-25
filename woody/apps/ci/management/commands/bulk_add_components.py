import os
import csv
from datetime import datetime
from optparse import make_option

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from apps.ci.models import CiCommonInfo, Device, Component

from utils import normalize_datetimefield, normalize_postiveintegerfield

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
			make_option('--import',
				action='store',
				dest='importfile',
				default=False,
				help='Bulk import components from .csv file'),
				)
	args = '''<realm>'''
	help = 'Bulk add components from a file'

	def handle(self, *args, **options):
		csvheader = ['name', 'device_id', 'vendor', 'ip_address',
					'component_id', 'connected_ports', 'shutdown_ports', 'n_of_ports', 
					'part', 'serial', 'fru_line_card', 'fru_route_mem', 'fru_packet_mem', 
					'l3_engine_type', 'l3_engine', 'tan', 'description', 'controller_mem', 
					'reserved_ports', 'cost', 'mgmt_ip_address', 
					'version', 'hostname']

		if not args[0]:
			self.stdout.write('Please specify the realm this import belongs to')
			sys.exit()

		realm = args[0]

		if not os.path.exists(options['importfile']):
			self.stdout.write('File does not exist. Please specify an existing csv file')
			sys.exit()

		csvfile = csv.DictReader(open(options['importfile'], 'rb'), fieldnames=csvheader, delimiter=',')
		for component in csvfile:
			# We need to delete some key:value pairs from the dict as they are not used in the component model
			REDUNDANTFIELDS = ['hostname', 'mgmt_ip_address', 'ip_address']
			for k in REDUNDANTFIELDS:
				del component[k]

			for i in ['connected_ports', 'shutdown_ports', 'n_of_ports', 'reserved_ports']:
				component[i] = normalize_postiveintegerfield(component[i])

			try:
				Component.objects.filter(serial=component['serial'], component_id=component['component_id']).update(last_seen=timezone.now(), **component)
				self.stdout.write('Component already exists. Updating component "%s %s"\n' % (component['name'], component['serial']))
			except Component.DoesNotExist:
				try:
					d = Device.objects.get(realm=realm, device_id=component['device_id'])
					c = d.component_set.create(first_seen=timezone.now(), last_seen=timezone.now(), **component)
					self.stdout.write('Successfully added component "%s" with serial %s\n' % (component['name'], component['serial']))
				except:
					self.stdout.write('Failed to add component "%s" with serial %s\n' % (component['name'], component['serial']))	