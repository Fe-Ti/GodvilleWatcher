from Core_GP import *
from tkinter import *

root = Tk()


startbutton=Button(root,text='Начать (д)опрашивать\nсервер')
startbutton.grid(column=0 , row=0 )
stopbutton=Button(root,text='Остановить (д)опрос')
stopbutton.grid(column=1 , row=0 )

tf=dict() # 
tf['Запрос имени'] = Label(root,text='Поле для\nимени аккаунта')
tf['Запрос имени'].grid(column=0 , row=1)
tf['Запрос ключа'] = Label(root,text='Поле для\nключа аккаунта')
tf['Запрос ключа'].grid(column=1 , row=1)


namentry= Entry(root) # account name entry
namentry.grid(column=0, row=2 )
keyentry= Entry(root) # account key entry
keyentry.grid(column=1 , row=2 )

enabled = 0 # flag for running
clickLock = 0 # flag for doubleclick protection

numbers=list("words,wood_cnt,t_level,quest_progress,max_health,level,inventory_num,inventory_max_num,health,godpower,exp_progress,distance,bricks_cnt,boss_power,ark_m,ark_f,arena_won,arena_lost".split(","))
strings=list("town_name,temple_completed_at,shop_name,savings_completed_at,savings,quest,name,motto,gold_approx,godname,gender,fight_type,diary_last,clan_position,clan,boss_name,aura,ark_completed_at,alignment".split(","))
objects=list("pet,activatables".split(",")) #inventory is not used
bools=list("expired,arena_fight".split(","))

allkeys = numbers+strings+objects+bools
#ruseq =list("Слов в книге,Дерева гофер,Уровень торговца,Прогресс задания,Максимальное здоровье,Уровень,Занято в мешке,Размер мешка,Здоровье,Прана,Прогресс уровня,Столб,Кирпичей,Мощь босса,М,Ж,Побед,Поражений,Город,Храм построен,Лавка,Лавка открыта,Сбережения,Задание,Имя героя,Девиз,Золота в карманах,Имя аккаунта,Пол героя,В,Свежая запись в дневнике,Гильдранг,Гильдия,Имя босса,Аура,Ковчег достроен,Мировоззрение,Питомец,Активируемые трофеи,Актуальность данных,Находится в пошаговом бою".split(","))

class strdata:
    def __init__(self,txt,posx,posy):
        
        self.lbl = Label(root,text=txt)
        self.lbl.grid(column=posx,row=posy)

    def upt(self,how):
        self.lbl.config(text=how)
        
c=0
for i in strings:
    cx=c//10
    cy=c%10
    tf[i] = strdata('loading',cx,cy+3)
    c+=1


def Drawer(info):
    global tf
    for i in strings:
        if i in info:
            tf[i].upt(info[i])
        
    


def refresh():
    global  namentry, keyentry

    name=str(namentry.get())
    key=str(keyentry.get())
    heroinfo=(GetData(name,key))
    print(heroinfo)
    return heroinfo

def stop(event):
    global enabled, clickLock
    enabled=0
    if clickLock==1:
        print ('Блокировка кнопки start снята')
    clickLock=0
    
    
def start(event):
    global enabled, clickLock
    enabled = 1
    startbutton.config(bg='red')
    def runner():
        global enabled
        if enabled==1:
            print('tic')
            Drawer(refresh())
            root.after(1000*90,runner)
            
    if clickLock<1:
        clickLock=1
        runner()
    else:
        print ('Кнопка заблокирована! нажмите stop для разблокировки')
    
startbutton.bind('<Button-1>',start)
stopbutton.bind('<Button-1>',stop)
root.mainloop()
