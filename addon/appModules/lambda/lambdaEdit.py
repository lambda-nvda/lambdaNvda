#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>

import speech
from displayModel import EditableTextDisplayModelTextInfo
import NVDAObjects.window.edit as edit
import comHelper
import controlTypes
import braille
import config
import textInfos
import ui
import api
from logHandler import log

#We used EditableTextDisplayModelTextInfo to render cursor when in white spaces
class LambdaEditorFlatTextInfo(EditableTextDisplayModelTextInfo) :
	def updateCaret(self):
		self.obj.invalidateCache()
		self.obj.redraw()
		self._setCaretOffset(self._startOffset)

#Broken implementation of EditTextInfo
class LambdaEditorTextInfo(edit.EditTextInfo) :
	
	#JVEditor Bug: can't move the caret to \n, force move to \r
	def move(self,unit,direction,endPoint=None):
		retval = super(LambdaEditorTextInfo,self).move(unit,direction,endPoint)
		if retval and unit == textInfos.UNIT_CHARACTER and endPoint == None :
			ti = self.copy()
			ti.expand(textInfos.UNIT_CHARACTER)
			if ti.text == '\n' :
				return super(LambdaEditorTextInfo,self).move(unit,direction,endPoint)
		return retval
	
	def updateCaret(self):
		self._setSelectionOffsets(self._startOffset,0)
		braille.handler.mainBuffer.clear()
		braille.handler.handleGainFocus(self.obj)


class LambdaEditField(edit.Edit):
	description = None
	name = None
	_editorClass = u'TJvEditor' 
	_LambdaObjName = 'lambda.lambdaobj'
	_oLambda = None
	editAPIVersion = 0
	
	def _get_TextInfo(self) :
		if self.windowClassName == self._editorClass :
		#Broken implementation of selection primitives in TJvEditor, fix with:
			if (config.conf['lambda']['brailleFlatMode']) :
				return LambdaEditorFlatTextInfo
			else : return LambdaEditorTextInfo
		else : return edit.EditTextInfo
			
	def getLambdaObj(self) :
		if self._oLambda : 
			return self._oLambda
		else  :
			self.empty = ''
			oLambda = comHelper.getActiveObject(self._LambdaObjName,dynamic=True)
			if (oLambda) :
				self._oLambda = oLambda
				self.empty = self._oLambda.getnone()
				return self._oLambda
		return None
			
	def say(self, msg):
		if msg == self.empty:
			return
		speech.speakText(msg)
		
	def event_valueChange(self) :
		braille.handler.handleUpdate(self)

	def event_caret(self) :
		super(edit.Edit, self).event_caret()
		self.detectPossibleSelectionChange()
		self.invalidateCache()
		self.redraw()
		#Ugly but it works... This fires more quickly than valueChange
		if config.conf['keyboard']['speakTypedCharacters']:
			s = self.getLambdaObj().getlastinsertedel(self.windowHandle, 1)
			speech.speakText(s)
		
	def event_gainFocus(self):
		s = self.getLambdaObj().getline(self.windowHandle, -1, -1)
		self.say(s)
		self.initAutoSelectDetection()
		braille.handler.handleGainFocus(self)

	def event_typedCharacter(self, ch):
		pass

	def script_caret_moveByCharacter(self, gesture):
		gesture.send()
		s = self.getLambdaObj().getchar(self.windowHandle, -1, -1)
		self.say(s)

	
	def script_caret_moveByLine(self, gesture):
		gesture.send()
		self.script_sayLine(gesture)
		
	def script_sayLine(self,gesture) :
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

	def script_caret_delete(self, gesture):
		self.script_caret_backspaceCharacter(gesture)
		#It loses focus - set focus on this window
		braille.handler.handleGainFocus(self)

	def script_sayAll(self, gesture):
		s = self.getLambdaObj().getall(self.windowHandle)
		self.say(s)
		
	def script_sayDuplicate(self,gesture) :
		gesture.send()
		line = self.getLambdaObj().getline(self.windowHandle, -1, -1)
		self.say(line)
		braille.handler.handleUpdate(self)
	
	def script_sayHighlighted(self, gesture):
		s = self.getLambdaObj().getselected(self.windowHandle)
		self.say(s)

	def script_switch_flatMode(self,gesture) :
		global config
		val = config.conf['lambda']['brailleFlatMode'] = not config.conf['lambda']['brailleFlatMode']
		#Translators: This is the API / DisplayMode approach for the editor window. It is a toggle (on/off)
		flatModeMessage = _("flat mode ")
		self.TextInfo = self._get_TextInfo()	
		ui.message(flatModeMessage + ((lambda x: _("on") if x else _("off"))(val)))
		braille.handler.mainBuffer.clear()
		braille.handler.handleGainFocus(self)
		
	
	def script_saySpecialHighlight(self, gesture):
		gesture.send()
		self.initAutoSelectDetection()
		self.script_sayHighlighted(gesture)
		braille.handler.handleUpdate(self)

	def initAutoSelectDetection(self):
		self.s = ''
		s = self.getLambdaObj().getselected(self.windowHandle)
		if s:
			self.s = s.strip().rstrip()

	def detectPossibleSelectionChange(self):
		s = self.getLambdaObj().gethighlightedtext(self.windowHandle)
		if not s:
			s = ''
		else :
			s = s.strip().rstrip()
		if len(s) > len(self.s):
			self.say(self.getSChunk(self.s,s) + ' ' + _('selected'))
		elif len(s) < len(self.s) and len(s) > 0:
			self.say(self.getSChunk(s,self.s) + ' ' + _('not selected'))
		self.s = s
	
	def getSChunk(self, oldm, newm) :
		if oldm in newm :
			return newm.replace(oldm,'',1)
		else : return newm
	
	

		
	__gestures = {'kb:control+shift+b': 'saySpecialHighlight',
	'kb:control+b': 'saySpecialHighlight',
	'kb:control+d':'sayDuplicate',
	'kb:alt+leftArrow': 'caret_moveByCharacter',
	'kb:alt+rightArrow': 'caret_moveByCharacter',
	'kb:nvda+downArrow': 'sayAll',
    'kb:nvda+a': 'sayAll',
	'kb:nvda+shift+upArrow': 'sayHighlighted',
	'kb:nvda+l': 'sayLine',
	'kb:nvda+shift+f': 'switch_flatMode',
	'kb:nvda+upArrow': 'sayLine',
	}