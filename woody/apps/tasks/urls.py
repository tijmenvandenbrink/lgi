from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.tasks.views',
	url(r'^$', 'index'),												#http://dev.com/profiles/
	url(r'^(?P<unique_id>[a-zA-Z0-9_\-\.]+)/$', 'profile_detail'),					#http://dev.com/profiles/upc-nl-nl-snmp-collect/
    url(r'^(?P<unique_id>[a-zA-Z0-9_\-\.]+)/(?P<uuid>\d+)/$', 'task_detail'),			#http://dev.com/profiles/upc-nl-nl-snmp-collect/201209271209/
)