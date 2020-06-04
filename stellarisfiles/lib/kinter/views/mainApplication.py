from tkinter import *
from .defineBrowser import DefineBrowser

class MainApplication(Frame):
    def __init__(self, parent, filepaths, localizations):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.filepaths = filepaths
        self.localizations = localizations

        self.defineBrowser = DefineBrowser(self, localizations)
        self.defineBrowser.loadFilepaths(filepaths)
        self.defineBrowser.pack()
