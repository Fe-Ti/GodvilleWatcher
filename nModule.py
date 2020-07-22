import Linotif
from tkinter import *

def notify(self,nText):
	if self.DND_t == 0:
		if self.platform =='Linux':
			Linotif.notify(self,nText)
		else:
			self.platform='fallback'
			
		if self.platform=='fallback':
			fallbackNotification(self,nText)


def fallbackNotification(self,nText):			
	self.notifWindow = Toplevel(self.root)
	self.notifWindow.geometry("+2+2")
	self.notifWindow.attributes('-topmost', True)
	self.notifWindow.title("Дозорный Годвилля") 
	self.notification = Label(self.notifWindow, text = nText,  justify=LEFT, anchor=W, wraplength=80*8)
	self.notification.pack()	
	self.notifWindow.after(self.notifcationTime, lambda: self.notifWindow.destroy()) # Destroy the widget after several seconds
