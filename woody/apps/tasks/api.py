from django.contrib.auth.models import User

from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from apps.tasks.models import Task, Profile

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'auth/user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
		authentication = BasicAuthentication()
		authorization = DjangoAuthorization()

class ProfileResource(ModelResource):
    class Meta:
		queryset = Profile.objects.all()
		resource_name = 'profile'
		authentication = BasicAuthentication()
		authorization = DjangoAuthorization()
		filtering = {
            'unique_id': ALL,
            'name': ALL,
            'realm': ALL,
            'firstseen': ALL,
            'lastseen': ALL,
            'active': ALL }

class TaskResource(ModelResource):
	profile = fields.ForeignKey(ProfileResource, 'profile')

	class Meta:
		queryset = Task.objects.all()
		resource_name = 'task'
		authentication = BasicAuthentication()
		authorization = DjangoAuthorization()
		filtering = {
            'profile': ALL_WITH_RELATIONS,
            'uuid': ALL,
            'polling_server': ALL,
            'start': ALL,
            'end': ALL
        }