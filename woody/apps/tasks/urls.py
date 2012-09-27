from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('apps.tasks.views',
	url(r'^$', 'index'),												#http://dev.com/profiles/
	url(r'^(?P<unique_id>[a-zA-Z0-9_\-]+)/$', 'profile_detail'),					#http://dev.com/profiles/upc-nl-nl-snmp-collect/
    url(r'^(?P<unique_id>[a-zA-Z0-9_\-]+)/(?P<uuid>\d+)/$', 'task_detail'),			#http://dev.com/profiles/upc-nl-nl-snmp-collect/201209271209/
    url(r'^static/.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)