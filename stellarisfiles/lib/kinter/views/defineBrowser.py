from tkinter import *
from .modules import *
from .. import eventReader
import os
from pprint import pprint

class DefineBrowser(Frame):

    def openFilepath(self, e):
        widget = e.widget
        index = widget.curselection()[0]
        filepath = widget.get(index)
        print ('You selected file', index, filepath)
        
        self.eventDefines.loadEvents(filepath)

    def loadFilepaths(self, filepaths):
        self.filepaths = filepaths
        self.fileList.replaceListItems(filepaths)

    def __init__(self, parent, localizations):
        Frame.__init__(self, parent)
        self.parent = parent
    
        self.fileList = FileList(self, [])
        self.fileList.grid(row=0, column=0)
        self.fileList.getListbox().bind("<<ListboxSelect>>", self.openFilepath)

        self.eventDefines = EventDefines(self, localizations)
        self.eventDefines.grid(row=0, column=1)

class EventDefines(Frame):

    def __init__(self, parent, localizations):
        Frame.__init__(self, parent)
        self.parent = parent 
        self.localizations = localizations

        self.eventsList = EventList(self, [])    
        self.eventsList.grid(row=0, column=0)    
        self.eventsList.getListbox().bind("<<ListboxSelect>>", self.loadEvent)

        self.eventView = EventView(self, None)
        self.eventView.grid(row=1, column=0)

        self.optionsList = OptionList(self, [])
        self.optionsList.grid(row=2, column = 0)

    def loadEvents(self, filepath):
        events = []
        eventIds = []
        self.events = eventReader.getEvents(filepath)
        eventsIds = eventReader.getEventIds(self.events, self.localizations)
        self.eventsList.replaceListItems(eventsIds)

    def loadEvent(self, e):
        widget = e.widget
        index = widget.curselection()[0]
        eventId = widget.get(index)
        
        print ('You selected event', index, eventId)
        event = self.events["events"][index]
        eventSummary =  eventReader.getEventSummary(event, self.localizations)
        
        self.eventView.loadEventSummary(eventSummary)
        
        optionNames = []
        for option in eventSummary["options"]:
            optionNames.append(option["name"])
        self.optionsList.replaceListItems(optionNames)

class FileList(PackedList):
    def __init__(self, parent, filepaths):
        # os.path.basename(your_path)
        PackedList.__init__(self, parent, "Files", filepaths, 50, 38)
        self.parent = parent

class EventList(PackedList):
    def __init__(self, parent, eventsNames):
        PackedList.__init__(self, parent, "Events", eventsNames, 50, 25)
        self.parent = parent

class EventView(Frame):

    def loadEventSummary(self, eventSummary):
        self.eventNameLabel["text"] = eventSummary["name"]
        self.eventDescription["text"] = eventSummary["description"]

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