
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def notify(self,nText):
	DBusGMainLoop(set_as_default=True)
	bus = dbus.SessionBus()
	notify = dbus.Interface((bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')), 'org.freedesktop.Notifications')

	name="Дозорный Годвилля"
	message=nText

	n = notify.Notify('Notify', 1, 'notification-message-im', name, message, [], [], self.notifcationTime)
