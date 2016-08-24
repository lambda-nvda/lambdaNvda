#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella <lapostadialberto@gmail.com>

import config
import os
import globalVars


PROFILE_NAME = "lambda"
#Translators: This string represents the file name of the Lambda braille table for the translated language. The file should be present in the "brailleTables" directory in this addon. The default is the italian braille translation table.
TABLE_NAME = _("lambda-ita.utb")

def profileExists() :
	try :
		(config.conf._getProfile(PROFILE_NAME))
		return True
	except :
		return False

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

def _getBrlTablePath(tableName) :
	return os.path.abspath(os.path.join(globalVars.appArgs.configPath, "addons", "Lambda", "appModules",PROFILE_NAME,"brailleTables",tableName))