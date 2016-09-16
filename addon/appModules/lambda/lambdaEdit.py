#Addon for Lambda Math Editor
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>

import addonHandler
import speech
from displayModel import EditableTextDisplayModelTextInfo
import NVDAObjects.window.edit as edit
import comHelper
import controlTypes
import braille
import config
import textInfos
import ui

addonHandler.initTranslation()

#We've used EditableTextDisplayModelTextInfo when user want white spaces to be rendered in braille.
class LambdaEditorFlatTextInfo(EditableTextDisplayModelTextInfo) :
	def updateCaret(self):
		self.obj.invalidateCache()
		self.obj.redraw()
		self._setCaretOffset(self._startOffset)

#Custom implementation of EditTextInfo because the Lambda editor seems to use different messages to set caret position.
class LambdaEditorTextInfo(edit.EditTextInfo) :
	#JVEditor Bug: can't move the caret to \n, force move to \r (for braille CR keys)
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

'''
Base class for Lambda edit fields with COM support. These controls shares the following behaviour:
* Speech is retrieved from the Lambda application through a COM object;
* Braille is rendered from textInfos.
'''
class LambdaEditField(edit.Edit):		
	scriptCategory = "Lambda"
	
	#Standard NVDAObject properties setters:
	description = None
	name = None
	_LambdaObjName = 'lambda.lambdaobj' #OLE Object name
	_oLambda = None #global object (use getLambdaObj to retrieve it)
	editAPIVersion = 0

	#OLE Lambda Object and convenient speak function
	def getLambdaObj(self) :
		if not self._oLambda : 
			self.empty = ''
			oLambda = comHelper.getActiveObject(self._LambdaObjName,dynamic=True)
			if (oLambda) :
				self._oLambda = oLambda
				self.empty = self._oLambda.getnone()
		return self._oLambda
			
	def say(self, msg):
		if msg == self.empty:
			return
		speech.speakText(msg)
	
	#Convinent scripts to reports text and selection
	def script_reportCurrentLine(self,gesture) :
		s = self.getLambdaObj().getline(self.windowHandle, -1, -1)
		self.say(s)
	#Translators: this is a custom implementation of the globalCommands gesture, it doesn't support spelling.
	script_reportCurrentLine.__doc__=_("Reports the current line under the application cursor.")
	
	def script_sayAll(self, gesture):
		s = self.getLambdaObj().getall(self.windowHandle)
		self.say(s)
	#Translators: Lambda can't read from the current caret position, the implementation of sayAll provided starts reading from the top of the document.
	script_sayAll.__doc__ = _("reads from the beginning of the document up to the end of the text.")	

	def script_reportCurrentSelection(self, gesture):
		s = self.getLambdaObj().getselected(self.windowHandle)
		self.say(s)
	#Translators: this is a custom implementation of the globalCommands gesture.
	script_reportCurrentSelection.__doc__=_("Announces the current selection in edit controls and documents.")	
	
	#Events section
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
		
	#Scripts to handle caret movements (editableText.EditableText)
	def script_caret_moveByCharacter(self, gesture):
		gesture.send()
		s = self.getLambdaObj().getchar(self.windowHandle, -1, -1)
		self.say(s)
		
	def script_caret_moveByLine(self, gesture):
		gesture.send()
		self.script_reportCurrentLine(gesture)

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

	#Selection detection
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
			self.say(self._getSChunk(self.s,s) + ' ' + _('selected'))
		elif len(s) < len(self.s) and len(s) > 0:
			self.say(self._getSChunk(s,self.s) + ' ' + _('not selected'))
		self.s = s
	
	def _getSChunk(self, oldmessage, newmessage) :
		if oldmessage in newmessage :
			return newmessage.replace(oldmessage,'',1)
		return newmessage
	
	#Gestures binding:
	__gestures = {
	#Lambda specific commands
	'kb:alt+leftArrow': 'caret_moveByCharacter',
	'kb:alt+rightArrow': 'caret_moveByCharacter',
	#SayAll override
	"kb(desktop):NVDA+downArrow": "sayAll",
	"kb(laptop):NVDA+a": "sayAll",
	#Report selection
	'kb(desktop):NVDA+shift+upArrow': 'reportCurrentSelection',
	'kb(laptop):NVDA+shift+s': 'reportCurrentSelection',
	#Say Line
	'kb(desktop):NVDA+upArrow': 'reportCurrentLine',
	'kb(laptop):NVDA+l': 'reportCurrentLine',
	}

'''
This class extends the LambdaEditField for calculator dialog.
'''
class LambdaDialogEdit(LambdaEditField):
	def script_caret_newLine(self,gesture) :
		#Prevents NVDA speaks the calculator result twice
		gesture.send()

'''
This class extends the LambdaEditField for matrix dialog.
'''
class LambdaMatrixEdit(LambdaEditField):
	TextInfo = LambdaEditorFlatTextInfo

		
'''
This class extends the LambdaEditField for the main editor. It adds scripts that can be used only in the main editor of Lambda.
'''
class LambdaMainEditor(LambdaEditField):
	def _get_TextInfo(self) :
		config.conf['lambda']['brailleFlatMode'] = str(config.conf['lambda']['brailleFlatMode']) == 'True'
		if config.conf['lambda']['brailleFlatMode'] :
			return LambdaEditorFlatTextInfo
		return LambdaEditorTextInfo
	
	#Lambda hotkeys
	def script_selectBlocks(self, gesture):
		gesture.send()
		self.initAutoSelectDetection()
		self.script_reportCurrentSelection(gesture)
		braille.handler.handleUpdate(self)
	#Translators: This is a Lambda hotkey ctrl+b extends the selection to the next surrounding block, ctrl+shift+b reduce the selection to a smaller block.
	script_selectBlocks.__doc__=_("Extends the selection to the surrounding block and reads it. If used with shift key, reduce the block and read it.")
	
	def script_sayDuplicate(self,gesture) :
		#Retrieves the line before sending gesture, duplicate line is the same as the current one.
		line = self.getLambdaObj().getline(self.windowHandle, -1, -1)
		gesture.send()
		braille.handler.handleUpdate(self)
		self.say(line)
	#Translators: This is a Lambda hotkey. ctrl+d is a macro that duplicates current line. The script reports the duplicated line.
	script_sayDuplicate.__doc__=_("Duplicates the current line and reads it")
	
	def script_switch_flatMode(self,gesture) :
		val = config.conf['lambda']['brailleFlatMode'] = not config.conf['lambda']['brailleFlatMode']
		#Translators: This determines whether to use API or DisplayMode to render the editor window on a braille display. It is a toggle (on/off)
		flatModeMessage = _("flat mode ")
		self.TextInfo = self._get_TextInfo()	
		ui.message(flatModeMessage + ((lambda x: _("on") if x else _("off"))(val)))
		braille.handler.mainBuffer.clear()
		braille.handler.handleGainFocus(self)
	#This script set the desired textInfo for braille, when flat mode is on, the LambdaEditorFlatTextInfo is used, otherwise the LambdaEditorTextInfo is set.
	script_switch_flatMode.__doc__=_("Toggle the braille flat mode on or off.")

	__gestures = {
	#Braille flat mode
	'kb:nvda+shift+f': 'switch_flatMode',
	#Lambda editor commands
	'kb:control+shift+b': 'selectBlocks',
	'kb:control+b': 'selectBlocks',
	'kb:control+d':'sayDuplicate',
	}