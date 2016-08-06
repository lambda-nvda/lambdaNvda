#A part of NonVisual Desktop Access (NVDA)
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016 Alberto Zanella

import config
import os
import globalVars
from logHandler import log

PROFILE_NAME = "lambda"
TABLE_NAME = "lambda-ita.utb"

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
	#Write profile
	lp["braille"] = brlcfg
	lp.write()
	#Update profile trigger
	trigs = config.conf.triggersToProfiles["app:"+PROFILE_NAME] = PROFILE_NAME
	#Update profile configs
	config.conf.saveProfileTriggers()

def _getBrlTablePath(tableName) :
	return os.path.join(globalVars.appArgs.configPath, "addons", "Lambda", "appModules",PROFILE_NAME,"brailleTables",tableName)