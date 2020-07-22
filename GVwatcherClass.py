from Core_GP import *
from tkinter import *
import time 
import platform
from notifCircumstances import * 
import nModule # handles all platform-dependent notification routine 



# Crystal v1.0 

class GV_WatchingCrystal:
	PARAMETERS = dict(zip('godname,godkey,enabled,dmax,DND_t,diary_t,quest_t,activatables_t,logdiary'.split(','),['','',0,10,0,0,0,0,0])) # defaults
	
	prevdiary = ''
	prevdiarynotif = ''
	prevquestnotif = ''
	prevactivnotif = ''
	counter=0
	notifcationTime=10000
	notifLine=''
	
	clickLock = 0 # flag for doubleclick protection

	numbers = list("words,wood_cnt,t_level,quest_progress,max_health,level,inventory_num,inventory_max_num,health,godpower,exp_progress,distance,bricks_cnt,boss_power,ark_m,ark_f,arena_won,arena_lost".split(","))
	strings = list("town_name,temple_completed_at,shop_name,savings_completed_at,savings,quest,name,motto,gold_approx,godname,gender,fight_type,diary_last,clan_position,clan,boss_name,aura,ark_completed_at,alignment".split(","))
	objects = list("pet,activatables".split(",")) #inventory is not used
	bools = list("expired,arena_fight".split(","))
	namebase = set()
	allkeys = numbers+strings+objects+bools
	alllabels = list("Слов в книге,Дерева для ковчега,Уровень торговца,Прогресс задания,Максимальное здоровье,Уровень,Занято в мешке,Размер мешка,Здоровье,Прана,Прогресс уровня,Столбов от столицы,Кирпичей,Мощь босса,М,Ж,Побед,Поражений,Город,Храм построен,Лавка,Лавка открыта,Сбережения,Задание,Имя,Девиз,Золота в карманах,Имя аккаунта,Пол героя,В,Свежая запись в дневнике,Гильдранг,Гильдия,Имя босса,Аура,Ковчег достроен,Характер,Питомец,Активируемые трофеи,Актуальность данных,Находится в пошаговом бою".split(","))
	labeleq =dict(zip(alllabels,allkeys))
	
	BG='#eeeeee'
	FG='#000000'
	
	statusLabels = "Имя.Девиз.Характер.Гильдия.Гильдранг.Уровень.Прогресс уровня.Занято в мешке.Размер мешка.Здоровье.Максимальное здоровье.Задание.Прогресс задания.Золота в карманах.Побед.Поражений.Дерева для ковчега.М.Ж.Сбережения.Столбов от столицы".split('.')
	
	counter=0
	
	info=dict()
	
	
	
	def __init__(self):
		try:
			initfile = open('GVW.init','r')
			line = initfile.readline()
			while line!='':
				line=line.split('=')
				name=line[0]
				val=line[1].replace('\n','')
				if val.isdigit():
					val=int(val)
				self.PARAMETERS[name]=val
				#print (line,name,val,self.PARAMETERS)
				line = initfile.readline()
			initfile.close()
		
		except FileNotFoundError:
			pass
		
		for i in self.PARAMETERS:
			setattr(self,i,self.PARAMETERS[i])
			
		self.platform = platform.system()
		
		self.root = Tk()
		self.root.title('GodvilleWatcher')
		
		self.initializeStatus()
		self.initializeControls()
		self.initialisediary()

		if self.godname!='' and self.godkey!='':
			self.updateInfo()
					
	def initializeStatus(self):

		self.Status = Frame(self.root,padx=1)
		self.Status.pack(side=LEFT,fill=Y)
		k=0
		self.heroStatusL=[]
		self.LabelValueKeys=[]
		self.ValLABELS=[]
		for i in self.statusLabels:
			self.heroStatusL.append(Label(self.Status, text=i+' : ', fg= self.FG, wraplength=20*8))
	
			self.heroStatusL[k].grid(sticky='w', column=0,row=k)
			
			
			self.LabelValueKeys.append(self.labeleq[i])
			self.ValLABELS.append(Label(self.Status, text='',wraplength=20*8, fg= self.FG))
			self.ValLABELS[k].grid(sticky='w', column=1,row=k)
			k+=1
			
		self.GValues = dict(zip(self.LabelValueKeys,self.ValLABELS))
	
	def initialisediary(self):	
		self.diaryL = Label(self.root, justify=LEFT, anchor=W, wraplength=80*8)
		self.diaryL.pack(side=TOP,fill=X)
		self.diary=[]
		for i in range (self.dmax):
			self.diary.append('')
	
	def initializeControls(self):				
		self.Controls = Frame(self.root)
		self.Controls.pack(side=TOP,fill=X)
		
		self.accframe = Frame(self.Controls)
		self.accframe.pack(fill=Y,side=LEFT)		
		
		self.namentryL = Label(self.accframe,text='Поле для\nимени аккаунта')
		self.namentryL.pack(fill=X,side=TOP)
		self.namentry = Entry(self.accframe) # account name entry
		self.namentry.pack(fill=X,side=TOP)
		self.namentry.insert(0,self.godname)
		
		self.keyentryL = Label(self.accframe,text='Поле для\nключа аккаунта')
		self.keyentryL.pack(fill=X,side=TOP)
		self.keyentry = Entry(self.accframe) # account key entry
		self.keyentry.pack(fill=X,side=TOP)
		self.keyentry.insert(0,self.godkey)
		
		self.otherc = Frame(self.Controls)
		self.otherc.pack(fill=Y,side=LEFT)
		
		self.startbutton = Button(self.otherc,text='START\n▶')
		self.startbutton.pack(fill=Y,side=LEFT)
		
		self.stopbutton = Button(self.otherc,text='STOP\n⫴⫴')
		self.stopbutton.pack(fill=Y,side=LEFT)
		
		self.savebutton = Button(self.otherc,text='SAVE\n⌻')
		self.savebutton.pack(fill=Y,side=LEFT)
		
		self.dmaxL = Label(self.otherc,text='diary max string count:')
		self.dmaxL.pack(fill=X,side=TOP)
		self.dmaxE = Entry(self.otherc)
		self.dmaxE.pack(fill=X,side=TOP)
		self.dmaxE.insert(0,self.dmax)
		
		self.statusLL = Label(self.otherc,text='Статус:')
		self.statusLL.pack(fill=X,side=TOP)
		self.statusL = Label(self.otherc,text='Остановлен', wraplength=30*8)
		self.statusL.pack(fill=X,side=TOP)

	def adddiaryString(self):
		#print(self.info['diary_last'])
		if self.prevdiary!=self.info['diary_last']:
			currtime = str(time.strftime("%H:%M",time.localtime()))+'  '
			self.diary.append(currtime + self.info['diary_last'])
			self.prevdiary=self.info['diary_last']
			self.diarystr=''
			for i in range(self.dmax):
				self.diarystr+= self.diary[-i] + '\n'

			self.diaryL.config(text=self.diarystr)
			
				
	
	
	def runner(self):
		
		if self.enabled == 1:
			
			self.clickLock = 1
			
			self.info = GetData(self.godname,self.godkey)			
			self.updateGValues()

			self.root.after(90*1000,self.runner)
		
		
	def updateInfo(self):
		
		#print(self.root.winfo_rootx())
		self.enabled = 1
		self.statusL.config(text='Запущен')
		
		if self.clickLock == 0:
			self.runner()
		else:
			self.statusL.config(text='Сначала остановите опрос сервера.')
	
	
	def notify(self,nText):
		nModule.notify(self,nText)
	
	def notifier(self):
		self.notifLine=''
		if diaryNotify(self):
			self.notifLine+='Дневник :\n'+self.info['diary_last']+'\n\n'
		if questNotify(self):
			self.notifLine+='Задание :  '+self.info['quest']+'\n\n'
		if activNotify(self):
			activatables = 'Активируемое:  '
			for i in self.info['activatables']:
				activatables+=i+'; '
			self.notifLine+=activatables+'\n'
		if expiredNotify(self):
			self.notifLine+='Данные устарели\n'
		if self.godkey!='' and self.notifLine!='':
			self.notify(self.notifLine)
			#print('ding-dong') # string for testing

	
	
	def stopW(self):
		self.enabled,self.clickLock = stopper(self)
		self.statusL.config(text='Остановлен')
		if self.logdiary == 1 and self.diary!=[]:
			dlf = open ('Diary_log.txt','a')
			s=self.godname + ' ' +self.info['name']+ '\n'
			for i in self.diary:
				if i!='':
					s+=i+'\n'
			dlf.write(s)
			dlf.close()
		
	def startW(self):
		self.enabled,_clickLock_ = starter(self)
		if self.godname!='':
			self.updateInfo()
	
	def updateGValues(self):
		for i in self.info:
			if i in self.GValues:
				self.GValues[i].config(text=self.info[i])
		if 'diary_last' in self.info:
			self.adddiaryString()
		self.notifier()
		
	
	def getGodname(self):
		self.godname=self.namentry.get()
		self.PARAMETERS['godname']= kkombo(self)

	def getGodkey(self):
		self.godkey=self.keyentry.get()
		self.PARAMETERS['godkey']=self.godkey
	def getDmax(self):
		self.dmax=int(self.dmaxE.get())
		self.PARAMETERS['dmax']=self.dmax
	def saveGG(self):
		initfile = open('GVW.init','w')
		print(self.PARAMETERS)
		self.PARAMETERS['enabled']=self.enabled
		s = ''
		for i in self.PARAMETERS:
			s+=i+'='+str(self.PARAMETERS[i])+'\n'
		initfile.write(s)
		initfile.close()
	
	def startGVW(self):
		self.root.mainloop()
	def terminateGVW(self):
		self.root.destroy()


