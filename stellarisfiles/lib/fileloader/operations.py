
import glob 
import os
import yaml
from pprint import pprint

from . import larkParser as parser

def GetFilenamesInFolder(directoryPath):
    eventFilepaths = glob.glob (os.path.join (directoryPath, "*.txt"))
    return [eventFilepath for eventFilepath in eventFilepaths]

def GetLocalizationContentsInFolder(localizationDirectorypath):
    localizationYamlPattern = os.path.join(localizationDirectorypath,"*.yml")
    localisationFilepaths = glob.glob(localizationYamlPattern)
    
    localizations = {}
    for localisationFilepath in localisationFilepaths:
        with open(localisationFilepath, 'r', encoding='utf-8-sig') as stream:
            try:
                print("Loading %s..." % localisationFilepath)
                localisationContent = yaml.load(stream, Loader=yaml.FullLoader)["l_english"]
                localizations.update(localisationContent)
                
            except yaml.YAMLError as exc:
                print(exc)
                
    return localizations

def GetLocalizationContentsFromFile(localisationFilepath):
    with open(localisationFilepath, 'r', encoding="utf-8-sig") as stream:
        try:
            print("Loading %s..." % localisationFilepath)
            return yaml.load(stream, Loader=yaml.FullLoader)["l_english"]
        except yaml.YAMLError as exc:
            print(exc)

def LoadStellarisFile(filepath):
    return parser.ParseEventFile(filepath)
