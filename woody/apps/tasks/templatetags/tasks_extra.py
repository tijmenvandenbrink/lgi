from django import template
from apps.tasks.models import Metric

register = template.Library()

@register.filter
def get_metric(metrics, arg):
	for m in metrics:
		if m.metric == arg:
			return m.value
	
    	return False

@register.filter
def get_profile_metric(metrics, arg):
    try:
        return metrics[arg]
    except KeyError:
        return False


@register.filter
def get_profile_stats(profile):
	from collections import defaultdict

	metrics = Metric.objects.filter(task__profile=profile, task__status="Success")
	z = defaultdict(list)
	for m in metrics:
		z[m.metric].append(int(m.value))

	result = {}

	for x in z:
		mean, std = _meanstdv(z[x])
		result[x] = { 'mean':mean, 'std':std }

	return result

def _meanstdv(x):
    """ Calculate mean and standard deviation of data x[]: mean = {\sum_i x_i \over n} std = sqrt(\sum_i (x_i - mean)^2 \over n-1) """
    from math import sqrt
    if len(x) == 0:
        mean, std = 0
    else:
        n, mean, std = len(x), 0, 0
        for a in x:
            #if not type(a) == int:
            #    log.error("Unsupported type: %s for %s", type(a), a)

            mean += int(a)
            #log.info("Subtotal mean: %s", mean)

        mean = mean / float(n)

        for a in x:
            std = std + (int(a) - mean)**2
            try:
                std = sqrt(std / float(n-1))
            except ZeroDivisionError:
                std = 0

    return mean, std