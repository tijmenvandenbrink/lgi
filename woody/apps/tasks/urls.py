from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tasks.views',
    url(r'^tasks/$', 'index'),
    url(r'^tasks/(?P<uuid>\d+)/$', 'detail'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

