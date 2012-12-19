from django.shortcuts import render_to_response, get_object_or_404

from apps.tasks.models import Profile, Task, Metric

def index(request):
	profiles_list = Profile.objects.all().order_by('realm')
	return render_to_response('profiles/index.html', {'profiles_list': profiles_list})

def realm_detail(request, realm):
	profiles_list = Profile.objects.all().order_by('realm')
	return render_to_response('profiles/realm_index.html', {'profiles_list': profiles_list})

def profile_detail(request, realm, name):
	profiles_list = Profile.objects.all().order_by('realm')
	p = get_object_or_404(Profile, realm=realm, name=name)
	task_list = p.task_set.all().order_by('-uuid')
	return render_to_response('profiles/detail.html', {'profiles_list': profiles_list, 
		                                               'profile': p, 
		                                               'task_list': task_list})

def task_detail(request, realm, name, uuid):
	profiles_list = Profile.objects.all().order_by('realm')
	p = get_object_or_404(Profile, realm=realm, name=name)
	t = get_object_or_404(Task, uuid=uuid, profile=p)
	metrics_list = Metric.objects.filter(task__uuid=uuid, task__profile=p)
	return render_to_response('tasks/detail.html', {'profiles_list': profiles_list, 
		                                            'metrics_list': metrics_list, 
		                                            'profile': p, 'task': t})