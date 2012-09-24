from django.contrib import admin
from apps.ci.models import Device, Component

class ComponentInline(admin.StackedInline):
    model = Component

class DeviceAdmin(admin.ModelAdmin):
	list_display = ('device_id', 'realm', 'vendor', 'timestamp', 
					'hostname', 'mgmt_ip_address', 
					'active')
	list_filter = ('realm', 'vendor', 'timestamp', 
					'active')
	search_fields = ['device_id', 'mgmt_ip_address']
	inlines = [ComponentInline]

class ComponentAdmin(admin.ModelAdmin):
	list_display = ('name', 'device_id', 'realm', 'vendor', 'timestamp',  
					'active')
	list_filter = ('realm', 'vendor', 'timestamp', 
					'active')
	search_fields = ['name', 'device_id']

admin.site.register(Device, DeviceAdmin)
admin.site.register(Component, ComponentAdmin)