from django.db import models

class Profile(models.Model):
	''' A profile is a blueprint of a task '''
	unique_id = models.CharField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	realm = models.CharField(max_length=255)
	first_seen = models.DateTimeField()
	last_seen = models.DateTimeField()
	active = models.BooleanField()

	def __unicode__(self):
		return u"%s-%s" % (self.realm, self.name)

class Task(models.Model):
	''' Task model for keeping track of tasks '''
	STATUSCHOICES = (('Success', 'Success'), ('Failed', 'Failed'))

	profile = models.ForeignKey(Profile)
	uuid = models.CharField(max_length=255)
	status = models.CharField(max_length=255, choices=STATUSCHOICES)
	polling_server = models.CharField(max_length=255)
	start = models.DateTimeField()
	end = models.DateTimeField()

	def duration(self):
		return u"%s" % (self.end - self.start)

	def __unicode__(self):
		return self.uuid

	class Meta:
		ordering = ['-uuid']
		get_latest_by = 'start'


class Metric(models.Model):
	''' Analytics model for keeping task metrics '''
	task = models.ForeignKey(Task)
	metric = models.CharField(max_length=255)
	value = models.IntegerField()

	def __unicode__(self):
		return u"%s" % (self.metric)