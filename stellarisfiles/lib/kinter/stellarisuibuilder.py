from tkinter import *
from . import uibuilder as uibuilder

def createEventHeader(root):
    eventHeader = Frame(root)

    eventIdLabel = uibuilder.createPackedLabel(eventHeader, "Event Id")
    eventNameLabel = uibuilder.createPackedLabel(eventHeader, "Event Name (Localization)")
    eventDescriptionHeaderLabel = uibuilder.createPackedLabel(eventHeader, "Event Description")
    eventDescriptionLabel = uibuilder.createPackedLabel(eventHeader, "Localized description...")

    return eventHeader

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