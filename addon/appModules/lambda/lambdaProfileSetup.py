#Addon for Lambda Math Editor
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
#Copyright (C) 2016-2017 Alberto Zanella <lapostadialberto@gmail.com>

brailleTablesLegacyImpl = False
import config
import os
import globalVars
import braille
import addonHandler
import sharedMessages as shMsg
import gui
from gui import guiHelper
from gui.settingsDialogs import SettingsDialog
import wx
try :
	import brailleTables
except ImportError :
	brailleTablesLegacyImpl = True #Backward compatibility NVDA < 2017.3

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
	setDefaultBraillevalues(brlcfg)
	#Write profile
	lp["braille"] = brlcfg
	lp.write()
	#Update profile trigger
	trigs = config.conf.triggersToProfiles["app:"+PROFILE_NAME] = PROFILE_NAME
	trigs = config.conf.triggersToProfiles[SIXDOTS_APP] = PROFILE_NAME
	#Update profile configs
	config.conf.saveProfileTriggers()


def setDefaultBraillevalues(brlcfg,translationTable = True,tetherTo = True,readByParagraph = True,wordWrap = True):
	if translationTable : brlcfg["translationTable"] = _getBrlTablePath(TABLE_NAME)
	if tetherTo : brlcfg["tetherTo"] = "focus"
	if readByParagraph : brlcfg["readByParagraph"] = False
	if wordWrap : brlcfg["wordWrap"]=False

#Contains custom braille tables for lambda
_lambdaBrailleTables = None
def getLambdaBrailleTables() :
	global _lambdaBrailleTables
	if _lambdaBrailleTables == None :
		_lambdaBrailleTables = tuple((_getBrlTablePath(file),file,False,) for file in os.listdir(_getBrlTablesDir()) if os.path.isfile(os.path.join(_getBrlTablesDir(), file)) and file.startswith("lambda-"))
	return _lambdaBrailleTables

# Adds the braille table to the list in braille settings dialog
def addBrailleTableToGUI():
	if brailleTablesLegacyImpl :
		return legacy_addBrailleTableToGUI()
	#Retrieves all tables in addon directory with prefix 'lamda-' and adds them to the global collection
	for table in getLambdaBrailleTables() :
			brailleTables.addTable(table[0],table[1],False,True,False)	


#Deprecated - Here for compatibility with NVDA < 2017.3
def legacy_addBrailleTableToGUI():
	#Retrieves all tables in addon directory with prefix 'lamda-'
	braille.TABLES = braille.TABLES + getLambdaBrailleTables()

# Removes the braille table to the list in braille settings dialog
def removeBrailleTableToGUI():
	if brailleTablesLegacyImpl :
		return legacy_removeBrailleTableToGUI()
	for table in getLambdaBrailleTables() :
		brailleTables._tables.pop(table[0])

#Deprecated - Here for compatibility with NVDA < 2017.3
def legacy_removeBrailleTableToGUI():
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


def onQuickProfileWizardDialog(evt) :
	gui.mainFrame._popupSettingsDialog(QuickProfileWizardDialog)

class QuickProfileWizardDialog(SettingsDialog):
	# Translators: This is the label for the Quick Profile Wizard dialog.
	# This dialog helps the user to reset relevant profile options without deleting his custom settings.
	title = _("Revert LAMBDA Profile Wizard")

	def makeSettings(self, settingsSizer):
		helper=guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: This is the static text of the Quick Profile Wizard dialog.
		msgIntro=_("Choose which options you want to reset to the default value for the Lambdas profile")
		self.introStxt=helper.addItem(wx.StaticText(self,-1,label=msgIntro))
		# Translators: This is the label for a checkbox in the
		# Quick Profile Wizard dialog.
		self.defaultTranslationTableCheckBox=helper.addItem(wx.CheckBox(self,wx.ID_ANY,label=_("Keep the LAMBDA braille table for the current language (%s)") % TABLE_NAME))
		self.defaultTranslationTableCheckBox.SetValue(True)
		# Translators: This is the label for a checkbox in the
		# Quick Profile Wizard dialog.
		self.brailleTetherToFocusCheckBox=helper.addItem(wx.CheckBox(self,wx.ID_ANY,label=_("Set the braille cursor to tether the focus")))
		self.brailleTetherToFocusCheckBox.SetValue(True)
		# Translators: This is the label for a checkbox in the
		# Quick Profile Wizard dialog.
		self.disableReadByParagraphCheckBox=helper.addItem(wx.CheckBox(self,wx.ID_ANY,label=_("Disable the Braille reading by paragraph")))
		self.disableReadByParagraphCheckBox.SetValue(True)
		# Translators: This is the label for a checkbox in the
		# Quick Profile Wizard dialog.
		self.disableBrailleWordWrapCheckBox=helper.addItem(wx.CheckBox(self,wx.ID_ANY,label=_("Disable word wrappping of the braille line")))
		self.disableBrailleWordWrapCheckBox.SetValue(True)

	def postInit(self):
		self.defaultTranslationTableCheckBox.SetFocus()

	def onOk(self,evt):
		lp = config.conf._getProfile(PROFILE_NAME,True)
		brlcfg = lp["braille"]
		setDefaultBraillevalues(brlcfg,self.defaultTranslationTableCheckBox.IsChecked(),self.brailleTetherToFocusCheckBox.IsChecked(),self.disableReadByParagraphCheckBox.IsChecked(),self.disableBrailleWordWrapCheckBox.IsChecked())
		lp.write()
		super(QuickProfileWizardDialog, self).onOk(evt)
