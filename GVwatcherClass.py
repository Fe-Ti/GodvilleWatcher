from Core_GP import *
from tkinter import *

# Crystal v1.0 

class GV_WatchingCrystal:
	godname=''
	godkey=''
	try:
		initfile = open('GVW.init','r')
		godname = initfile.readline().replace('\n','')
		godkey = initfile.readline().replace('\n','')
		enabled = (initfile.readline().replace('\n',''))
		dmax = (initfile.readline().replace('\n',''))
		if enabled!='' and dmax!='':
			enabled = int(enabled)
			dmax = int(dmax)
		initfile.close()
	
	except FileNotFoundError:
		enabled = 0 # flag for running
		dmax = 10 # dairy max
		pass
	notifcationTime=5000
	
	clickLock = 0 # flag for doubleclick protection

	numbers=list("words,wood_cnt,t_level,quest_progress,max_health,level,inventory_num,inventory_max_num,health,godpower,exp_progress,distance,bricks_cnt,boss_power,ark_m,ark_f,arena_won,arena_lost".split(","))
	strings=list("town_name,temple_completed_at,shop_name,savings_completed_at,savings,quest,name,motto,gold_approx,godname,gender,fight_type,diary_last,clan_position,clan,boss_name,aura,ark_completed_at,alignment".split(","))
	objects=list("pet,activatables".split(",")) #inventory is not used
	bools=list("expired,arena_fight".split(","))

	allkeys = numbers+strings+objects+bools
	alllabels = list("Слов в книге,Дерева для ковчега,Уровень торговца,Прогресс задания,Максимальное здоровье,Уровень,Занято в мешке,Размер мешка,Здоровье,Прана,Прогресс уровня,Столбов от столицы,Кирпичей,Мощь босса,М,Ж,Побед,Поражений,Город,Храм построен,Лавка,Лавка открыта,Сбережения,Задание,Имя,Девиз,Золота в карманах,Имя аккаунта,Пол героя,В,Свежая запись в дневнике,Гильдранг,Гильдия,Имя босса,Аура,Ковчег достроен,Характер,Питомец,Активируемые трофеи,Актуальность данных,Находится в пошаговом бою".split(","))
	labeleq =dict(zip(alllabels,allkeys))
	
	BG='#eeeeee'
	FG='#000000'
	
	statusLabels = "Имя.Девиз.Характер.Гильдия.Гильдранг.Уровень.Прогресс уровня.Занято в мешке.Размер мешка.Здоровье.Максимальное здоровье.Задание.Прогресс задания.Золота в карманах.Побед.Поражений.Дерева для ковчега.М.Ж.Сбережения.Столбов от столицы".split('.')
	
	counter=0
	
	info=dict()
	
	def __init__(self):
		self.root = Tk()
		self.root.title('GodvilleWatcher')
		#self.root.geometry('800x400')
		self.initializeStatus()
		self.initializeControls()
		self.initialiseDairy()

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
			self.heroStatusL.append(Label(self.Status, text=i+' : ', fg= self.FG))
	
			self.heroStatusL[k].grid(sticky='w', column=0,row=k)
			
			
			self.LabelValueKeys.append(self.labeleq[i])
			self.ValLABELS.append(Label(self.Status, text='',wraplength=20*8, fg= self.FG))
			self.ValLABELS[k].grid(sticky='w', column=1,row=k)
			k+=1
			
		self.GValues = dict(zip(self.LabelValueKeys,self.ValLABELS))
	
	def initialiseDairy(self):	
		self.Dairy = Label(self.root, justify=LEFT, anchor=W, wraplength=80*8)
		self.Dairy.pack(side=TOP,fill=X)
		self.dairy=[]
	
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
		
		self.dmaxL = Label(self.otherc,text='Dairy max string count:')
		self.dmaxL.pack(fill=X,side=TOP)
		self.dmaxE = Entry(self.otherc)
		self.dmaxE.pack(fill=X,side=TOP)
		self.dmaxE.insert(0,self.dmax)
		
		self.statusLL = Label(self.otherc,text='Статус:')
		self.statusLL.pack(fill=X,side=TOP)
		self.statusL = Label(self.otherc,text='Остановлен')
		self.statusL.pack(fill=X,side=TOP)

	def addDairyString(self):
		print(self.info['diary_last'])
		self.dairy.append(self.info['diary_last'])
		self.dairystr=''
		
		if len(self.dairy)>self.dmax:
			
			for i in range(self.dmax):
				self.dairystr+=self.dairy[-i]
		
		else:
			
			for i in range(len(self.dairy)):
				self.dairystr=self.dairy[i]+'\n'+self.dairystr
		self.Dairy.config(text=self.dairystr)
	
	
	def runner(self):
		
		if self.enabled == 1:
			
			self.clickLock = 1
			
			self.info = GetData(self.godname,self.godkey)			
			self.updateGValues()

			self.root.after(60*1000,self.runner)
		
		
	def updateInfo(self):
		
		print(self.root.winfo_rootx())
		self.enabled = 1
		self.statusL.config(text='Запущен')
		
		if self.clickLock == 0:
			self.runner()
		else:
			print('Сначала остановите опрос сервера.')
	
	def notify(self,nText):
		self.notifWindow = Toplevel(self.root)
		self.notifWindow.geometry("+2+2")
		self.notifWindow.title("Дозорный Годвилля")
		#nitifTitle = Label(notifWindow, text = "Дозорный Годвилля", justify=LEFT, anchor=W, wraplength=80*8)
		#nitifTitle.pack() 
		self.notification = Label(self.notifWindow, text = nText,  justify=LEFT, anchor=W, wraplength=80*8)
		self.notification.pack()
		
		self.notifWindow.after(self.notifcationTime, lambda: self.notifWindow.destroy()) # Destroy the widget after 30 seconds
		#self.root.after(60*1000,self.runner)
	
	def stopW(self):
		self.enabled = 0
		self.clickLock = 0
		self.statusL.config(text='Остановлен')
		
	def startW(self):
		self.updateInfo()
	
	def updateGValues(self):
		for i in self.info:
			if i in self.GValues:
				self.GValues[i].config(text=self.info[i])
		if 'diary_last' in self.info:
			self.addDairyString()
			self.notify(self.info['diary_last'])
	
	def getGodname(self):
		self.godname=self.namentry.get()
	def getGodkey(self):
		self.godkey=self.keyentry.get()
	def getDmax(self):
		self.dmax=int(self.dmaxE.get())
	def saveGG(self):
		initfile = open('GVW.init','w')
		s = self.godname+'\n'+self.godkey+'\n'+str(self.enabled)+'\n'+str(self.dmax)+'\n'
		initfile.write(s)
		initfile.close()
	
	def start(self):
		self.root.mainloop()



