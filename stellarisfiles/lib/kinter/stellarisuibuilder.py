from tkinter import *
from . import uibuilder as uibuilder
from .. import fileloader as fileloader 
from . import eventReader as eventReader
from pprint import pprint

def openEvents(e):
    widget = e.widget
    index = widget.curselection()[0]
    value = widget.get(index)
    print ('You selected item', index, value)
    events = fileloader.LoadStellarisFile(value)
    for event in events["events"]:
        if "id" in event:
            print(event["id"])
    

def createEventView(root, eventSummary):
    pprint(eventSummary)
    eventView = LabelFrame(root)
    eventLabel = uibuilder.createPackedLabel(eventView, "Event")
    eventNameLabel = uibuilder.createPackedLabel(eventView, eventSummary["name"])
    eventDescription = uibuilder.createPackedLabel(eventView, eventSummary["description"])
    return eventView

def createConversationForm(root):
    conversationForm = Frame(root)

    eventVarLabel = uibuilder.createPackedLabel(conversationForm, "anomaly.1000")
    eventVarLabel.pack()

    conversationVarnameField = uibuilder.createTextField(conversationForm, "Varname", 1)
    conversationVarnameField.pack()

    conversationNameField = uibuilder.createTextField(conversationForm, "Name", 1)
    conversationNameField.pack()

    conversationDescriptionField = uibuilder.createTextField(conversationForm, "Description", 1)
    conversationDescriptionField.pack()

    conversationEthicField = uibuilder.createTextField(conversationForm, "Ethic", 1)
    conversationEthicField.pack()

    conversationDemandsField = uibuilder.createTextField(conversationForm, "Demands", 10)
    conversationDemandsField.pack()

    return conversationForm

def createFileList(root, files):
    # for item in files:
    #     listbox.insert(END, item)
    # listbox.bind("<<ListboxSelect>>", openEvents)
    return uibuilder.createList(root, "Files", files, 50, 25)   

def createEventList(root, events):
    return uibuilder.createList(root, "Events", events, 50, 25)
    
def getEvents(filepath):
    return fileloader.LoadStellarisFile(filepath)

def createOptionList(root, options):
    return uibuilder.createList(root, "Options", options, 50, 8)

def createEventViewer(root, filepaths, localisations):
    eventViewer = Frame(root)
    
    fileList= createFileList(eventViewer, filepaths)
    fileList.grid(row=0, column=0)

    events = []
    eventIds = []
    if len(filepaths) >= 1:
        events = getEvents(filepaths[1])
        eventsIds = eventReader.getEventIds(events, localisations)

    eventsPanel = Frame(eventViewer)
    eventsPanel.grid(row=0, column=1)
    
    eventsList = createEventList(eventsPanel, eventsIds)    
    eventsList.grid(row=0, column=0)        

    event = {}
    if len(filepaths) >= 1:
        event = events["events"][0]

    eventSummary =  eventReader.getEventSummary(event, localisations)
    eventView = createEventView(eventsPanel, eventSummary)
    eventView.grid(row=1, column=0)

    optionsList = createOptionList(eventsPanel, eventSummary["options"])
    optionsList.grid(row=2, column = 0)

    return eventViewer