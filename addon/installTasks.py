#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>



import addonHandler
import gui
import wx
import config

addonHandler.initTranslation()


## Translators: title of the message box that appears when the user is installing the addon and an older version prevents the update to be completed.
oldaddontitle = _('Incompatible version of the addon detected')

## Translators: text of the message box that appears when the user is installing the addon and an older version prevents the update to be completed.
oldaddonmsg = _("""An old, incompatible version of this addon has been detected.
This prevents the installation to be completed.
Please uninstall the previous version before proceeding with the Lambda addon setup.
""")

## Translators: title of the message box that appears when user is installing the addon in NVDA and a "lambda" profile is already present. 
profilefoundtitle = _('lambda profile already exists')

## Translators: text of the message box that appears when user is installing the addon in NVDA and a "lambda" profile is already present. 
profilefoundmsg = _("""Another profile named "lambda" is already present in your NVDA configuration. 
This may prevents the addon on create and configure the lambda profile correctly.
Please review default options for this addon using the Revert LAMBDA Profile Wizard (pressing nvda+alt+r) while the Lambda Application is active.
Press OK to complete the addon Setup.
""")

def onInstall():
	if "Lambda" in [a.name for a in addonHandler.getAvailableAddons()] :
		gui.messageBox(oldaddonmsg,oldaddontitle)
		raise Exception("Old version prevents the update to be completed.")
	
	try :
		if config.conf._getProfile("lambda") :
			gui.messageBox(profilefoundmsg,profilefoundtitle)
	except : return
    
