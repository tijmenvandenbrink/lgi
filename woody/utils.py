from datetime import datetime
import pytz

def normalized_datetimefield(s):
	if s == '':
		return None
	else:
		try:
			d = datetime.strptime(s, '%m/%d/%y %H:%M:%S')
			return d.replace(tzinfo=pytz.UTC)
		except:
			return None

def normalized_postiveintegerfield(i):
	if i == '':
		return 0
	else:
		return i