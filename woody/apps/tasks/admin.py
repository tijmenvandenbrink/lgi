from django.contrib import admin
from apps.tasks.models import Profile, Task, Metric

class TaskInline(admin.TabularInline):
    model = Task

class MetricInline(admin.TabularInline):
	model = Metric

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'realm', 'first_seen', 
					'last_seen', 'active')
	list_filter = ('name', 'realm', 'first_seen', 'last_seen', 
					'active')
	search_fields = ['name', 'realm']
	inlines = [TaskInline]

class TaskAdmin(admin.ModelAdmin):
	list_display = ('uuid', 'status', 'start', 'end')
	list_filter = ('uuid', 'status', 'start', 'end')
	search_fields = ['uuid', 'status']
	inlines = [MetricInline]

class MetricAdmin(admin.ModelAdmin):
	list_display = ('metric', 'value')
	list_filter = ('metric', 'value')
	search_fields = ['metric']	

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Metric, MetricAdmin)