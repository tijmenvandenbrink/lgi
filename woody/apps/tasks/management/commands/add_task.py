import os
import csv
import pdb
from datetime import datetime
from optparse import make_option

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from apps.tasks.models import Profile, Task, Metric

from utils import normalize_datetimefield

class Command(BaseCommand):
	args = '''<profile name> <realm> <uuid> <status> <polling_server> <start> <end>'''
	help = '''Add task in the form:\n
			profilenamex domainx 12394394 Success pollingserverx "yyyy/mm/dd HH:MM:SS" "yyyy/mm/dd HH:MM:SS" 
	'''

	def handle(self, *args, **options):
		profile_unique_id = '%s-%s' % (args[1].lower(), args[0].lower())
		try:
			p = Profile.objects.get(unique_id=profile_unique_id)
			self.stdout.write('Profile already exists "%s"\n' % (p))
		except Profile.DoesNotExist:
			p = Profile(unique_id=profile_unique_id, name=args[0], realm=args[1], 
				first_seen=timezone.now(), last_seen=timezone.now(), active=True)
			p.save()
			self.stdout.write('Profile did not exist. Created profile "%s"\n' % (p))
		
		fi = p.task_set.filter(uuid=args[2])
		if len(fi) == 0:
			try:
				t = p.task_set.create(uuid=args[2], status=args[3], polling_server=args[4], start=normalize_datetimefield(args[5]), end=normalize_datetimefield(args[6]))
				self.stdout.write('Successfully added task "%s" to profile %s\n' % (t.uuid, p))
			except:
				pdb.set_trace()
				self.stdout.write('Failed to add task "%s" to profile %s\n' % (t.uuid, p))
		else:
			self.stdout.write('Task already exists "%s %s"\n' % (p, fi[0].uuid))			