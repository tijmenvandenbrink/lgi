from django.conf.urls import patterns, include, url
from tastypie.api import Api
from apps.tasks.api import UserResource, ProfileResource, TaskResource, MetricResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ProfileResource())
v1_api.register(TaskResource())
v1_api.register(MetricResource())

urlpatterns = patterns('apps.tasks.views',
	url(r'^$', 'index'),												#http://dev.com/profiles/
    url(r'^(?P<realm>[a-zA-Z0-9_\-\.]+)/$', 'realm_detail'),
	url(r'^(?P<realm>[a-zA-Z0-9_\-\.]+)/(?P<name>[a-zA-Z0-9_\-\.]+)/$', 'profile_detail'),					#http://dev.com/profiles/upc-nl-nl-snmp-collect/
    url(r'^(?P<realm>[a-zA-Z0-9_\-\.]+)/(?P<name>[a-zA-Z0-9_\-\.]+)/(?P<uuid>\d+)/$', 'task_detail'),			#http://dev.com/profiles/upc-nl-nl-snmp-collect/201209271209/
    url(r'^api/', include(v1_api.urls)),
)