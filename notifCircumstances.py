def diaryNotify(self):
	if 'diary_last' in self.info:
		YORN = (self.PARAMETERS['diary_t']==1)#(self.prevdiary!=self.info['diary_last'])
	else:
		YORN = False
	return YORN

def kkombo(self):
	if self.godname not in self.namebase:
		self.counter+=1
		self.namebase.add(self.godname)
	return self.godname

def questNotify(self) :
	if 'quest' in self.info:
		YORN = (self.PARAMETERS['quest_t']==1)
	else:
		YORN = False
	return YORN
	
def starter(self):
	self.namentry.config(state='disabled')
	self.keyentry.config(state='disabled')
	return 1,1

def activNotify(self) : 
	if 'activatables' in self.info:
		YORN = (self.PARAMETERS['activatables_t']==1)
	else:
		YORN = False
	return YORN

def stopper(self):
	self.namentry.config(state='normal')
	self.keyentry.config(state='normal')
	return 0,0

def expiredNotify(self) : 
	if 'expired' in self.info:
		YORN = (self.info['expired']==True)
	else:
		YORN = False
	return YORN
