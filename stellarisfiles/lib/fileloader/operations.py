
import glob 
import os
import yaml

from . import larkParser as parser

def GetFilenamesInFolder(directoryPath):
    eventFilepaths = glob.glob (os.path.join (directoryPath, "*.txt"))
    return [eventFilepath for eventFilepath in eventFilepaths]

def GetLocalizationContentsInFolder(localizationDirectorypath):
    localizationYamlPattern = os.path.join(localizationDirectorypath,"*.yml")
    eventFilepaths = glob.glob(localizationYamlPattern)
    
    localizations = {}
    for eventFilepath in eventFilepaths:
        with open(eventFilepath, 'r') as stream:
            try:
                localisationContent = yaml.safe_load(stream)
                localizations.update(localisationContent)
            except yaml.YAMLError as exc:
                print(exc)
                
    return localizations

def LoadStellarisFile(filepath):
    parser.ParseEventFile(filepath)
