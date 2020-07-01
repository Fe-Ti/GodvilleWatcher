from GVwatcherClass import *

app = GV_WatchingCrystal()

def startWFE(event):
	app.startW()
def stopWFE(event):
	app.stopW()
def saveGGFE(event):
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
app.namentry.bind('<Key>',getGodnameFE)
app.keyentry.bind('<Key>',getGodkeyFE)
app.dmaxE.bind('<Key>',getDmaxFE)

app.start()
