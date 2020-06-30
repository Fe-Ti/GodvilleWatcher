from Core_GP import *
from tkinter import *

class GV_WatchingCrystal:
	godname=''
	godkey=''
	try:
		initfile = open('API.init','r')
		godname = initfile.readline().replace('\n','')
		godkey = initfile.readline().replace('\n','')
		enabled = int(initfile.readline().replace('\n',''))
		dmax = int(initfile.readline().replace('\n',''))
		initfile.close()
	
	except FileNotFoundError:
		enabled = 0 # flag for running
		pass
		
	
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
		self.root.geometry('800x400')
		self.initializeStatus()
		self.initialiseDairy()
		self.initializeControls()
		if self.godname!='':
			self.startbutton.config(text='Успешно запущен!'
			self.updateInfo()
			self.root.after(5000,self.updateGValues())
		
	def initializeStatus(self):

		self.Status = Frame(self.root,padx=1, bg = self.BG)
		self.Status.pack(side=LEFT,fill=Y)
		k=0
		self.heroStatusL=[]
		self.LabelValueKeys=[]
		self.ValLABELS=[]
		for i in self.statusLabels:
			self.heroStatusL.append(Label(self.Status, text=i+' : ', bg = self.BG, fg= self.FG))
	
			self.heroStatusL[k].grid(sticky='w', column=0,row=k)
			
			
			self.LabelValueKeys.append(self.labeleq[i])
			self.ValLABELS.append(Label(self.Status, text='', bg = self.BG, fg= self.FG))
			self.ValLABELS[k].grid(sticky='w', column=1,row=k)
			k+=1
			
		self.GValues = dict(zip(self.LabelValueKeys,self.ValLABELS))
	
	def initialiseDairy(self):	
		self.Dairy = Label(self.root, bg = self.BG)
		self.Dairy.pack(side=TOP,fill=X)
		self.dairy=[]

	
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
	
	def initializeControls(self):				
		self.Controls = Frame(self.root, bg = self.BG)
		self.Controls.pack(side=TOP,fill=X)
		
		self.tf=dict() # 
		self.tf['Запрос имени'] = Label(self.Controls,text='Поле для\nимени аккаунта')
		self.tf['Запрос имени'].grid(column=0 , row=1)
		self.tf['Запрос ключа'] = Label(self.Controls,text='Поле для\nключа аккаунта')
		self.tf['Запрос ключа'].grid(column=1 , row=1)

		self.namentry= Entry(self.Controls) # account name entry
		self.namentry.grid(column=0, row=2 )
		self.namentry.insert(0,self.godname)
		
		self.keyentry= Entry(self.Controls) # account key entry
		self.keyentry.grid(column=1 , row=2 )
		self.keyentry.insert(0,self.godkey)
		
		self.startbutton=Button(self.Controls,text='Начать (д)опрашивать сервер')
		self.startbutton.grid(column=0 , row=0 )
		self.stopbutton=Button(self.Controls,text='Остановить (д)опрос')
		self.stopbutton.grid(column=1 , row=0 )
		
	
	def updateInfo(self):
		
		self.enabled = 1
		
		def runner():
			
			if self.enabled == 1:
				
				self.clickLock = 1
				
				self.info = GetData(self.godname,self.godkey)			
				self.updateGValues()
				
				self.root.after(60*1000,runner)
		if self.clickLock == 0:
			runner()
		else:
			print('LOCKED!!!')
				
	def updateGValues(self):
		for i in self.info:
			if i in self.GValues:
				self.GValues[i].config(text=self.info[i])
		self.addDairyString()

	def start(self):
		self.root.mainloop()
	
	pass


app = GV_WatchingCrystal()
app.start()
