#Addon for Lambda Math Editor
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>

import config
import os
import globalVars
import braille
import addonHandler

addonHandler.initTranslation()

PROFILE_NAME = "lambda"
#Translators: This string is the file name of the Lambda braille table for the translated language. The file should be present in the "brailleTables" directory in this addon. The default is the italian braille translation table.
TABLE_NAME = _("lambda-ita.utb")

# Check whether the lambda profile already exists
def profileExists() :
	try :
		(config.conf._getProfile(PROFILE_NAME))
		return True
	except :
		return False

'''
Creates a new profile lambda.ini. By default it is of the form:

[braille]
	translationTable = table\path\tableName
	tetherTo = focus
	readByParagraph = False

[lambda]
	brailleFlatMode = True
'''
def createLambdaProfile() :
	config.conf.createProfile(PROFILE_NAME)
	config.conf.save()
	lp = config.conf._getProfile(PROFILE_NAME,True)
	#Creates braille config
	brlcfg = {}
	brlcfg["translationTable"] = _getBrlTablePath(TABLE_NAME)
	brlcfg["tetherTo"] = "focus"
	brlcfg["readByParagraph"] = False
	#lambda entry
	lcfg = {}
	lcfg['brailleFlatMode'] = True
	#Write profile
	lp["braille"] = brlcfg
	lp['lambda'] = lcfg
	lp.write()
	#Update profile trigger
	trigs = config.conf.triggersToProfiles["app:"+PROFILE_NAME] = PROFILE_NAME
	#Update profile configs
	config.conf.saveProfileTriggers()

# Adds the braille table to the list in braille settings dialog
def addBrailleTableToGUI():
	braille.TABLES = braille.TABLES + ((_getBrlTablePath(TABLE_NAME),TABLE_NAME,False,),)

# Retrieves the current absolute path for the braille table and updates the profile entry (useful for portable NVDA)
def updateTablePath() :
	basepath = os.path.abspath(globalVars.appArgs.configPath)
	lp = config.conf._getProfile(PROFILE_NAME,True)
	if basepath not in lp["braille"]["translationTable"] : #Directory has been moved
		lp["braille"]["translationTable"] = _getBrlTablePath(TABLE_NAME)
		lp.write()	
    
# Gets the absolute path of the braille table for the current language
def _getBrlTablePath(tableName) :
	return os.path.abspath(os.path.join(globalVars.appArgs.configPath, "addons", "lambda", "appModules",PROFILE_NAME,"brailleTables",tableName))