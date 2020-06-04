from tkinter import *
from .modules import *
from .. import eventReader

class DefineBrowser(Frame):

    def loadFilepaths(self, filepaths):
        self.filepaths = filepaths
        self.fileList.replaceListItems(filepaths)

    def __init__(self, parent, localizations):
        Frame.__init__(self, parent)
        self.parent = parent
    
        self.fileList = FileList(self, [])
        self.fileList.grid(row=0, column=0)

        self.eventDefines = EventDefines(self)
        self.fileList.grid(row=0, column=1)

class EventDefines(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent 

        self.eventsList = EventList(self, [])    
        self.eventsList.grid(row=0, column=0)    

        self.eventView = EventView(self, None)
        self.eventView.grid(row=1, column=0)

        self.optionsList = OptionList(self, [])
        self.optionsList.grid(row=2, column = 0)

    def loadEvents(self, filepath, localizations):
        events = []
        eventIds = []
        if len(filepaths) >= 1:
            events = eventReader.getEvents(filepath)
            eventsIds = eventReader.getEventIds(events, localizations)
        
        self.events = events

        self.eventsList = EventList(self, eventsIds)    
        self.eventsList.grid(row=0, column=0)  

    def loadEvent(self, event, localizations):
        eventSummary =  eventReader.getEventSummary(event, localizations)
        self.eventView = EventView(self, eventSummary)
        
        optionNames = []
        for option in eventSummary["options"]:
            optionNames.append(option["name"])

        self.optionsList = OptionList(self, optionNames)

class FileList(PackedList):
    def __init__(self, parent, filepaths):
        PackedList.__init__(self, parent, "Files", filepaths, 50, 25)
        self.parent = parent

class EventList(PackedList):
    def __init__(self, parent, eventsNames):
        PackedList.__init__(self, parent, "Events", eventsNames, 50, 25)
        self.parent = parent

class EventView(Frame):

    def loadEventSummary(self, eventSummary):
        self.eventLabel = PackedLabel(self, "Event")
        self.eventNameLabel = PackedLabel(self, eventSummary["name"])
        self.eventDescription = PackedLabel(self, eventSummary["description"])

    def __init__(self, parent, eventSummary):
        Frame.__init__(self, parent)
        self.eventLabel = PackedLabel(self, "Event")
        self.eventNameLabel = PackedLabel(self, "Name")
        self.eventDescription = PackedLabel(self, "Description")
        self.parent = parent

class OptionList(PackedList):
    def __init__(self, parent, optionNames):
        PackedList.__init__(self, parent, "Options", optionNames, 50, 8)
        self.parent = parent