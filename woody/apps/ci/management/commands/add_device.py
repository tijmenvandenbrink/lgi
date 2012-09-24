import pdb

from optparse import make_option

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from apps.ci.models import CiCommonInfo, Device

class Command(BaseCommand):
	args = '''<device_id realm vendor mgmt_ip_address [timestamp, 
														active=True, 
														hostname,
														ip_address, 
														sysname,
														description,
														contact,
														location,
														last_update_by_cli,
														last_update_by_snmp,
														chassis_type,
														hardware_version,
														hardware_id,
														rom_version,
														rom_system_version,
														configuration_register,
														memory,
														configuration_memory_in_use,
														boot_image,
														processor,
														os_version,
														hw_model,
														os_family]...>'''
	help = 'Adds the specified device'

	def handle(self, *args, **kwargs):

		unique_id = '%s-%s' % (args[1], args[0])
		try:
			device = Device.objects.get(pk=unique_id)

			# Do some update logic here
			self.stdout.write('Successfully updated device "%s"\n' % args[0])
		except Device.DoesNotExist:
			pdb.set_trace()
			d = Device(unique_id=unique_id,
						device_id=args[0],
						realm=args[1],
						vendor=args[2],
						mgmt_ip_address=args[3],
						ip_address=args[3],
						timestamp=timezone.now(),
						last_update_by_snmp=timezone.now(),
						last_update_by_cli=timezone.now())
			d.save()

			self.stdout.write('Successfully added device "%s"\n' % args[0])