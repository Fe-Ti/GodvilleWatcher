import urllib.request
from urllib.parse   import quote

def heroparser(data):
	# begin preparing data
	data = data[1:-1]

	numbers=list("words,wood_cnt,t_level,quest_progress,max_health,level,inventory_num,inventory_max_num,health,godpower,exp_progress,distance,bricks_cnt,boss_power,ark_m,ark_f,arena_won,arena_lost".split(","))
	strings=list("town_name,temple_completed_at,shop_name,savings_completed_at,savings,quest,name,motto,gold_approx,godname,gender,fight_type,diary_last,clan_position,clan,boss_name,aura,ark_completed_at,alignment".split(","))
	objects=list("pet,activatables".split(",")) #not used : inventory
	bools=list("expired,arena_fight".split(","))
	
	petnum=["pet_level"]
	petstr=["pet_class","pet_name"]
	petbool=["wounded"]
	
	info=dict()
	
	for parameter in numbers:
		
		exists=data.find('"'+parameter+'"')

		if exists>-1:
			bvalue = data.find(':',exists)
			evalue = data.find(',"',exists)
			info[parameter]=(data[bvalue+1:evalue])

	for parameter in strings:
		
		exists=data.find('"'+parameter+'"')

		if exists>-1:
			bvalue = data.find(':',exists)
			evalue = data.find(',"',exists)
			info[parameter]=data[bvalue+2:evalue-1]

	for parameter in bools:

		exists=data.find('"'+parameter+'"')

		if exists>-1:
			bvalue = data.find(':',exists)
			evalue = data.find(',"',exists)
			info[parameter]=(data[bvalue+1:evalue])        
	
	for parameter in objects:

		exists=data.find('"'+parameter+'"')

		if exists>-1:

			info[parameter]=dict()
			
			bvalue = data.find(':',exists)
			if data[bvalue+1]=='{':
				evalue = data.find('},"',exists)

				for petpar in petnum:
					
					pexists=data.find('"'+petpar+'"')
					if pexists>-1:
						bpvalue = data.find(':',pexists)
						epvalue = data.find(',"',pexists)
						info[parameter][petpar]=(data[bpvalue+1:epvalue].replace('}',''))

				for petpar in petbool:

					pexists=data.find('"'+petpar+'"')

					if pexists>-1:
						bpvalue = data.find(':',pexists)
						epvalue = data.find(',"',pexists)
						info[parameter][petpar]=(data[bpvalue+1:epvalue].replace('}','')) 

				for petpar in petstr:
		
					pexists=data.find('"'+petpar+'"')

					if pexists>-1:
						bpvalue = data.find(':',pexists)
						epvalue = data.find(',"',pexists)
						info[parameter][petpar]=data[bpvalue+2:epvalue-1].replace('}','')

			elif data[bvalue+1]=='[':
				evalue = data.find('],"',exists)
				info[parameter]= data[bvalue+2:evalue].replace(']','')


	# end setting var-s
	
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
