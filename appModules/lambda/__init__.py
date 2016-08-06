import appModuleHandler
import speech
from NVDAObjects.behaviors import EditableTextWithAutoSelectDetection
import comHelper
import controlTypes
import braille
import config
from . import lambdaProfileSetup as lp

class AppModule(appModuleHandler.AppModule):
	
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		if not (lp.profileExists()) :
			lp.createLambdaProfile()
	
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if (obj.windowClassName == u'TJvEditor') or (obj.windowClassName == u'TLambdaEdit') :  
			clsList.insert(0, LambdaEditField)
		if  (obj.windowClassName == u'TEdit') and (controlTypes.STATE_READONLY in obj.states) :
			clsList.insert(0, LambdaEditField)
			
class LambdaEditField(EditableTextWithAutoSelectDetection):
	description = None
	name = None
	COMCLASS = 'lambda.lambdaobj'
	l = None
	def getLambdaObj(self) :
		if self.l : 
			return self.l
		else  :
			l = comHelper.getActiveObject(self.COMCLASS,dynamic=True)
			if (l) :
				self.l = l
				self.empty = self.l.getnone()
				return self.l
			else :
				self.empty = ''
		return None
			
	def say(self, what):
		if what == self.empty:
			return
		speech.speakText(what)

	def event_gainFocus(self):
		s = self.getLambdaObj().getline(self.windowHandle, -1, -1)
		self.say(s)
		self.initAutoSelectDetection()
		braille.handler.handleGainFocus(self)

	def event_valueChange(self):
		l = self.getLambdaObj()
		if config.conf['keyboard']['speakTypedCharacters']:
			s = l.getlastinsertedel(self.windowHandle, 1)
			speech.speakText(s)
		braille.handler.handleUpdate(self)

	def event_typedCharacter(self, ch):
		pass

	def script_caret_moveByCharacter(self, gesture):
		gesture.send()
		s = self.getLambdaObj().getchar(self.windowHandle, -1, -1)
		self.say(s)

	def script_caret_moveByLine(self, gesture):
		gesture.send()
		s = self.getLambdaObj().getline(self.windowHandle, -1, -1)
		self.say(s)

	def script_caret_moveByWord(self, gesture):
		gesture.send()
		s = self.getLambdaObj().getword(self.windowHandle, -1, -1)
		self.say(s)

	def script_caret_moveByParagraph(self, gesture):
		self.script_caret_moveByLine(gesture)

	def script_caret_backspaceCharacter(self, gesture):
		gesture.send()
		s = self.getLambdaObj().getlastdeleted(self.windowHandle)
		self.say(s)
		braille.handler.handleUpdate(self)

	def script_caret_delete(self, gesture):
		self.script_caret_backspaceCharacter(gesture)
		braille.handler.handleUpdate(self)

	def script_sayAll(self, gesture):
		s = self.getLambdaObj().getall(self.windowHandle)
		self.say(s)
	
	def script_sayLIne(self,gesture) :
		s = self.getLambdaObj().getline(self.windowHandle, -1, -1)
		self.say(s)
		
	def script_sayHighlighted(self, gesture):
		s = self.getLambdaObj().getselected(self.windowHandle)
		self.say(s)

	def script_saySpecialHighlight(self, gesture):
		gesture.send()
		self.initAutoSelectDetection()
		self.script_sayHighlighted(gesture)
		braille.handler.handleUpdate(self)

	def initAutoSelectDetection(self):
		self.s = ''
		s = self.getLambdaObj().getselected(self.windowHandle)
		if s:
			self.s = s

	def detectPossibleSelectionChange(self):
		s = self.getLambdaObj().gethighlightedtext(self.windowHandle)
		if not s:
			s = ''
		if len(s) > len(self.s):
			self.say(_('selected') + ' ' + s[len(self.s):len(s)])
		elif len(s) < len(self.s):
			self.say(_('not selected') + ' ' + self.s[len(s):len(self.s)])
		self.s = s

		
	__gestures = {'kb:control+shift+b': 'saySpecialHighlight',
	'kb:control+b': 'saySpecialHighlight',
	'kb:alt+leftArrow': 'caret_moveByCharacter',
	'kb:alt+rightArrow': 'caret_moveByCharacter',
	'kb:nvda+downArrow': 'sayAll',
    'kb:nvda+a': 'sayAll',
	'kb:nvda+shift+upArrow': 'sayHighlighted',
	'kb:nvda+l': 'sayLIne',
    'kb:nvda+upArrow': 'sayLIne',
	}