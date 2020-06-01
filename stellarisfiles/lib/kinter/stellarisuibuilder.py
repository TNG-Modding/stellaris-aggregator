from tkinter import *
from . import uibuilder as uibuilder
from .. import fileloader as fileloader 
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

def getEventIds(events, localisations):
    ids = []
    for event in events["events"]:
        if "title" in event and event["title"] in localisations:
            eventId = event["id"]
            eventTitle = event["title"]
            ids.append("%s -- %s" % (eventId, localisations[eventTitle]))
        elif "id" in event:
            ids.append(event["id"])
    return ids

def getEventSummary(event, localisations):
    eventSummary = {}
    pprint(event)
    if "title" in event:
        if event["title"] in localisations:
            eventSummary["name"] = "%s -- %s" % (event["id"], localisations[event["title"]])
        else:
            eventSummary["name"] = "%s" % (event["id"])
    else:
        eventSummary["name"] = "No title"

    if "desc" in event:
        eventDesc = event["desc"]
        if not isinstance(eventDesc, str):
            eventDesc = eventDesc["text"] 

        if eventDesc in localisations:
            eventSummary["description"] = localisations[eventDesc]
        else: 
            eventSummary["description"] = eventDesc
    else:
        eventSummary["description"] = "No description"

    return eventSummary

def createOptionList(root, options):
    return uibuilder.createList(root, "Options", options, 50, 8)

def createEventViewer(root, filepaths, localisations):
    eventViewer = Frame(root)
    
    fileList= createFileList(eventViewer, filepaths)
    fileList.grid(row=0, column=0)

    events = []
    eventIds = []
    if len(filepaths) >= 1:
        events = getEvents(filepaths[0])
        eventsIds = getEventIds(events, localisations)

    eventsPanel = Frame(eventViewer)
    eventsPanel.grid(row=0, column=1)
    
    eventsList = createEventList(eventsPanel, eventsIds)    
    eventsList.grid(row=0, column=0)        

    eventSummary = getEventSummary(events["events"][1], localisations)
    eventView = createEventView(eventsPanel, eventSummary)
    eventView.grid(row=1, column=0)

    optionsList = createOptionList(eventsPanel, ["Option A"])
    optionsList.grid(row=2, column = 0)

    return eventViewer