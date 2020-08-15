import urllib.request
from urllib.parse   import quote
import json

def heroparser(data):
	info = json.loads(data)
	return info

def stopper(self):
	self.namentry.config(state='normal')
	self.keyentry.config(state='normal')
	return 0,0	

def kkombo(self):
	if self.godname not in self.namebase:
		self.counter+=1
		self.namebase.add(self.godname)
	return self.godname

def GetURL(url): # got from some site, added utf-8 decoding
	print(url)
	s = 'error'
	try:
		f = urllib.request.urlopen(url)
		s = f.read().decode('UTF-8','strict')
	except urllib.error.HTTPError:
		s = 'connect error'
	except urllib.error.URLError:
		s = 'url error'
	return s

def starter(self):
	self.namentry.config(state='disabled')
	self.keyentry.config(state='disabled')
	return 1,1

def GetData(name,key): 
	data = (GetURL('https://godville.net/gods/api/'+quote(name+'/'+key)))
	print(data)
	heroinfo=heroparser(data)
	#print(heroinfo)
	return heroinfo
