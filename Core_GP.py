import urllib.request
from urllib.parse   import quote
import json

def heroparser(data):
	info = json.loads(data)
	return info

def GetURL(url): # got from some site, added utf-8 decoding
	s = 'error'
	try:
		f = urllib.request.urlopen(url)
		s = f.read().decode('UTF-8','strict')
	except urllib.error.HTTPError:
		s = 'connect error'
	except urllib.error.URLError:
		s = 'url error'
	return s

def GetData(name,key): 
	data = (GetURL('https://godville.net/gods/api/'+quote(name+'/'+key)))
	print(data)
	heroinfo=heroparser(data)
	#print(heroinfo)
	return heroinfo
