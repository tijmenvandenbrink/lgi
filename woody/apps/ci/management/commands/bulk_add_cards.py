import os
import csv
import pdb
from datetime import datetime

from optparse import make_option

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from apps.ci.models import CiCommonInfo, Device, Component

class Command(BaseCommand):
	option_list = BaseCommand.option_list + (
			make_option('--import',
				action='store',
				dest='importfile',
				default=False,
				help='Bulk import cards from .csv file'),
				)
	args = '''<realm>'''
	help = 'Bulk adds cards from a file'

	def handle(self, *args, **options):
		csvheader = ['name', 'device_id', 'vendor', 'ip_address',
					'component_id', 'connected_ports', 'shutdown_ports', 'n_of_ports', 
					'part', 'serial', 'fru_line_card', 'fru_route_mem', 'fru_packet_mem', 
					'l3_engine_type', 'l3_engine', 'tan', 'description', 'controller_mem', 
					'reserved_ports', 'cost', 'mgmt_ip_address', 
					'version', 'hostname']

		realm = args[0]

		if os.path.exists(options['importfile']):
			csvfile = csv.DictReader(open(options['importfile'], 'rb'), fieldnames=csvheader, delimiter=',')
			for card in csvfile:
				# We need to delete some key:value pairs from the dict as they are not used in the component model 
				del card['hostname']
				del card['mgmt_ip_address']
				del card['ip_address']

				for i in ['connected_ports', 'shutdown_ports', 'n_of_ports', 'reserved_ports']:
					if card[i] == '':
						card[i] = 0

				try:
					c = Component.objects.get(serial=card['serial'])
					self.stdout.write('Card already exists "%s"\n' % card['name'])
				except Component.DoesNotExist:
					try:
						d = Device.objects.get(realm=realm, device_id=card['device_id'])
						c = d.component_set.create(timestamp=timezone.now(), **card)
					except:
						pdb.set_trace()

					self.stdout.write('Successfully added card "%s" with serial %s\n' % (card['name'], card['serial']))