from tkinter import *
from .defineBrowser import DefineBrowser
from .conversationBrowser import ConversationBrowser

class MainApplication(Frame):
    def __init__(self, parent, filepaths, conversations, localizations):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.filepaths = filepaths
        self.localizations = localizations

        self.defineBrowser = DefineBrowser(self, localizations)
        self.defineBrowser.loadFilepaths(filepaths)
        self.defineBrowser.grid(row=0,column=0)

        self.conversationBrowser = ConversationBrowser(self)
        self.conversationBrowser.loadConversations(conversations)
        self.conversationBrowser.grid(row=0,column=1)
