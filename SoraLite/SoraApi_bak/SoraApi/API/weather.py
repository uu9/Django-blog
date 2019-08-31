import requests
import django
from . import getordefault


def weather(request, ct=None):
	ct = getordefault(request, "ct", None)
	if ct is not None:
		r = requests.get('https://www.tianqiapi.com/api/?version=v1)', {"city": ct})
		rd = r.json()
		return rd
	else:
		r = requests.get('https://www.tianqiapi.com/api/?version=v1')
		rd = r.json()
		return rd
