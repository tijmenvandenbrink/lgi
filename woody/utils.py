from datetime import datetime
import pytz

def normalize_datetimefield(s):
	if s == '':
		return None
	else:
		try:
			d = datetime.strptime(s, '%Y/%m/%d %H:%M:%S')
			return d.replace(tzinfo=pytz.UTC)
		except:
			return None

def normalize_postiveintegerfield(i):
	if i == '':
		return 0
	else:
		return i