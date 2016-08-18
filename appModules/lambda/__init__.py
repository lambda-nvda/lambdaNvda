#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>

import appModuleHandler
import controlTypes
from . import lambdaProfileSetup as lp
from lambdaEdit import LambdaEditField


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