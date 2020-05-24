import glob

def GetFilesInCurrentFolder():
    eventFilepaths = glob.glob("*.txt")
    return ["./" + eventFilepath for eventFilepath in eventFilepaths]