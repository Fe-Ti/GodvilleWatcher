try:
	import dbus
	from dbus.mainloop.glib import DBusGMainLoop
	importerror = 0
except ModuleNotFoundError:
	importerror = 1
	
if importerror==0:
	def notify(self,nText):
		DBusGMainLoop(set_as_default=True)
		bus = dbus.SessionBus()
		notify = dbus.Interface((bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')), 'org.freedesktop.Notifications')

		name="Дозорный Годвилля"
		message=nText

		n = notify.Notify('Notify', 1, 'notification-message-im', name, message, [], [], self.notifcationTime)
else:
	def notify(self,nText):
		self.platform = 'fallback'
		
