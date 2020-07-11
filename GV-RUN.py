from GVwatcherClass import *

app = GV_WatchingCrystal()

def startWFE(event):
	app.getGodname()
	app.getGodkey()
	app.getDmax()
	app.startW()
def stopWFE(event):
	app.stopW()
	
def saveGGFE(event):
	app.getGodname()
	app.getGodkey()
	app.getDmax()
	app.saveGG()
	
def getGodnameFE(event):
	app.getGodname()
def getGodkeyFE(event):
	app.getGodkey()
def getDmaxFE(event):
	app.getDmax()

app.startbutton.bind('<ButtonRelease>',startWFE)
app.stopbutton.bind('<ButtonRelease>',stopWFE)
app.savebutton.bind('<ButtonRelease>',saveGGFE)
app.namentry.bind('<Return>',getGodnameFE)
app.keyentry.bind('<Return>',getGodkeyFE)
app.dmaxE.bind('<Return>',getDmaxFE)

app.startGVW()
