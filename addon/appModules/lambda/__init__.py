#Addon for Lambda Math Editor
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>

import addonHandler
import appModuleHandler
import controlTypes
from . import lambdaProfileSetup
from lambdaEdit import LambdaDialogEdit,LambdaMainEditor
from NVDAObjects.window import DisplayModelEditableText

addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):
	
# Dialogs which has edit fields like the main Lambda Editor
	_customDialogsNames = (
	"TStructureW", #Structure view Window
	"TFrm_Matrix", #Matrix Window
	"TFrm_Calculator_Simple", #Calculator 
	)
	
	def __init__(self, *args, **kwargs):
		super(AppModule, self).__init__(*args, **kwargs)
		if  (lambdaProfileSetup.profileExists()) :
			#We update the table abs path since the user should have a portable version and the path may be different.
			lambdaProfileSetup.updateTablePath()
		else: #If a lambda profile doesn't exists:
			lambdaProfileSetup.createLambdaProfile()
		
		lambdaProfileSetup.addBrailleTableToGUI()
	
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if (obj.windowClassName == u'TJvEditor') : #Main editor windows
			clsList.insert(0, LambdaMainEditor)
		if  (obj.windowClassName == u'TEdit') and (obj.role == controlTypes.ROLE_EDITABLETEXT) :
			#Dialogs with enhanced spoken math text
			try :
				dialogW = obj.parent.parent
				if dialogW and dialogW.windowClassName in self._customDialogsNames :
					clsList.insert(0, LambdaDialogEdit)
					clsList.remove(DisplayModelEditableText)
			except : pass
		if obj.windowClassName == u'TLambdaEdit' :
		#Matrix dialog
			try :
				dialogW = obj.parent.parent
				if dialogW and dialogW.windowClassName in self._customDialogsNames :
					clsList.insert(0, LambdaMatrixEdit)
					clsList.remove(DisplayModelEditableText)
			except : pass
	
	def terminate(self) :
		super(AppModule, self).terminate()
		#Clean-up custom braille tables
		lambdaProfileSetup.removeBrailleTableToGUI()