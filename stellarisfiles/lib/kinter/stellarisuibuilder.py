from tkinter import *
from . import uibuilder as uibuilder
from .. import fileloader as fileloader 

def createEventHeader(root):
    eventHeader = Frame(root)

    eventIdLabel = uibuilder.createPackedLabel(eventHeader, "Event Id")
    eventNameLabel = uibuilder.createPackedLabel(eventHeader, "Event Name (Localization)")
    eventDescriptionHeaderLabel = uibuilder.createPackedLabel(eventHeader, "Event Description")
    eventDescriptionLabel = uibuilder.createPackedLabel(eventHeader, "Localized description...")

    return eventHeader

def openEvents(e):
    widget = e.widget
    index = widget.curselection()[0]
    value = widget.get(index)
    print ('You selected item', index, value)
    events = fileloader.LoadStellarisFile(value)
    for event in events["events"]:
        if "id" in event:
            print(event["id"])
    

def createEventOptionsList(root):
    return uibuilder.createList(root, "Options", ["Option A"])

def createEventView(root):
    eventView = LabelFrame(root)

    eventHeader = createEventHeader(eventView)
    eventHeader.grid(row=0, column=0)

    eventOptionsList = createEventOptionsList(eventView)
    eventOptionsList.grid(row=0, column=1)

    createConversationButton = Button(eventView, text="Create Conversation")
    createConversationButton.grid(row=1, column=1)

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

def createFileView(root, name, files):
    frame = Frame(root)

    listLabel = uibuilder.createPackedLabel(frame, name)

    listbox = Listbox(frame)
    listbox.pack()

    for item in files:
        listbox.insert(END, item)
    listbox.bind("<<ListboxSelect>>", openEvents)
    return frame

def createEventList(root, events):
    return uibuilder.createList(root, "Events", events)
    
def getEvents(filepath, localisations):
    events = fileloader.LoadStellarisFile(filepath)
    ids = []
    for event in events["events"]:
        if "title" in event and event["title"] in localisations:
            eventId = event["id"]
            eventTitle = event["title"]
            ids.append("%s -- %s" % (eventId, localisations[eventTitle]))
        elif "id" in event:
            ids.append(event["id"])

    return ids

def createEventViewer(root, filepaths, localisations):
    eventViewer = Frame(root)
    filesFrame = createFileView(eventViewer, "Files", filepaths)
    filesFrame.grid(row=0, column=0)

    events = []
    if len(filepaths) >= 1:
        events = getEvents(filepaths[0], localisations)
        
    eventsFrame = createEventList(eventViewer, events)    
    eventsFrame.grid(row=0, column=1)        

    eventView = createEventView(eventViewer)
    eventView.grid(row=0, column=2)
    return eventViewer