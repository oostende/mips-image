from Screens.MessageBox import MessageBox

class ServiceStopScreen:
	def __init__(self):
		try:
			self.session
		except:
			print "[ServiceStopScreen] ERROR: no self.session set"
			
		self.oldref = None
		self.onClose.append(self.__onClose)
		
	def stopService(self):		
		self.oldref = self.session.nav.getCurrentlyPlayingServiceReference()
		self.session.nav.stopService()
		
	def __onClose(self):
		self.session.nav.playService(self.oldref)
		
	def restoreService(self, msg = _("Zap back to previously tuned service?")):
		if self.oldref:
			self.session.openWithCallback(self.restartPrevService, MessageBox, msg, MessageBox.TYPE_YESNO)
		else:
			self.restartPrevService(False)
		
	def restartPrevService(self, yesno):
		if not yesno:
			self.oldref=None
		self.close()