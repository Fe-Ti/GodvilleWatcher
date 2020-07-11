def diaryNotify(self):
	if 'diary_last' in self.info:
		YORN = (self.PARAMETERS['diary_t']==1)#(self.prevdiary!=self.info['diary_last'])
	else:
		YORN = False
	return YORN

def questNotify(self) :
	if 'quest' in self.info:
		YORN = (self.PARAMETERS['quest_t']==1)
	else:
		YORN = False
	return YORN

def activNotify(self) : 
	if 'activatables' in self.info:
		YORN = (self.PARAMETERS['activatables_t']==1)
	else:
		YORN = False
	return YORN

def expiredNotify(self) : 
	if 'expired' in self.info:
		YORN = (self.info['expired']==True)
	else:
		YORN = False
	return YORN
