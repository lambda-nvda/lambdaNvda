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
SIXDOTS_APP = "app:sixdots"

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
	#lcfg = {}
	#lcfg['brailleFlatMode'] = True
	#Write profile
	lp["braille"] = brlcfg
	#lp['lambda'] = lcfg
	lp.write()
	#Update profile trigger
	trigs = config.conf.triggersToProfiles["app:"+PROFILE_NAME] = PROFILE_NAME
	trigs = config.conf.triggersToProfiles[SIXDOTS_APP] = PROFILE_NAME
	#Update profile configs
	config.conf.saveProfileTriggers()

# Adds the braille table to the list in braille settings dialog
def addBrailleTableToGUI():
	#Retrieves all tables in addon directory with prefix 'lamda-'
	newTables = tuple((_getBrlTablePath(file),file,False,) for file in os.listdir(_getBrlTablesDir()) if os.path.isfile(os.path.join(_getBrlTablesDir(), file)) and file.startswith("lambda-"))
	braille.TABLES = braille.TABLES + newTables

# Removes the braille table to the list in braille settings dialog
def removeBrailleTableToGUI():
	braille.TABLES = tuple(table for table in braille.TABLES if not table[1].startswith("lambda-"))

# Retrieves the current absolute path for the braille table and updates the profile entry (useful for portable NVDA)
def updateTablePath() :
	lp = config.conf._getProfile(PROFILE_NAME,True)
	#If a system table has been selected, do not force the abspath
	if "lambda-" not in lp["braille"]["translationTable"] : return
	basepath = _getBrlTablesDir()
	tablename = os.path.basename(lp["braille"]["translationTable"])
	if basepath not in lp["braille"]["translationTable"]: #Directory has been moved
		lp["braille"]["translationTable"] = _getBrlTablePath(tablename)
		lp.write()

# Gets the absolute path of the braille table in tableName
def _getBrlTablePath(tableName) :
	return os.path.join(_getBrlTablesDir(),tableName)
	
#Get the absolute path to the brailleTables directory
def _getBrlTablesDir() :
	return os.path.abspath(os.path.join(globalVars.appArgs.configPath, "addons", "lambda", "appModules",PROFILE_NAME,"brailleTables"))