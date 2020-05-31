
import glob 
import os
import yaml

from . import larkParser as parser

def GetFilenamesInFolder(directoryPath):
    eventFilepaths = glob.glob (os.path.join (directoryPath, "*.txt"))
    return [eventFilepath for eventFilepath in eventFilepaths]

def GetLocalizationContentsInFolder(localizationDirectorypath):
    localizationYamlPattern = os.path.join(localizationDirectorypath,"*.yml")
    localisationFilepaths = glob.glob(localizationYamlPattern)
    
    localizations = {}
    for localisationFilepath in localisationFilepaths:
        with open(localisationFilepath, 'r') as stream:
            try:
                localisationContent = yaml.load(stream, Loader=yaml.FullLoader)
                localizations.update(localisationContent["l_english"])
            except yaml.YAMLError as exc:
                print(exc)
                
    return localizations

def GetLocalizationContentsFromFile(localisationFilepath):
    with open(localisationFilepath, 'r') as stream:
        try:
            return yaml.load(stream, Loader=yaml.FullLoader)["l_english"]
        except yaml.YAMLError as exc:
            print(exc)

def LoadStellarisFile(filepath):
    return parser.ParseEventFile(filepath)
