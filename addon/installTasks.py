#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>



import addonHandler
import gui
import wx
import config

addonHandler.initTranslation()

## Translators: message box when user is installing the addon in NVDA and a "lambda" profile is already present. 
profilefoundmsg = _("""Another profile named "lambda" is already present in your NVDA configuration. 
This prevents the addon on create and configure the lambda profile correctly.
If you want the addon to configure a lambda profile for you, please delete the old one named "lambda" using the NVDA "Configuration Profiles" dialog.
The new profile will be created the next time you'll start the Lambda app.
Otherwise please edit your profile configuration file manually.
""")

def onInstall():
	try :
		if config.conf._getProfile("lambda") :
			gui.messageBox(profilefoundmsg)
	except : return
    
