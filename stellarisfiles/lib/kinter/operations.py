from tkinter import *
from . import uibuilder as uibuilder
from . import stellarisuibuilder as stellarisuibuilder

def createWindow(files):
    root = Tk()

    eventViewer = Frame(root)
    eventViewer.grid(row=0, column=0)

    filesFrame = uibuilder.createList(eventViewer, "Files", files)
    filesFrame.grid(row=0, column=0)

    eventsFrame = uibuilder.createList(eventViewer, "Events", [])
    eventsFrame.grid(row=0, column=1)

    eventView = stellarisuibuilder.createEventView(eventViewer)
    eventView.grid(row=0, column=2)

    # Conversation
    conversationEditor = Frame(root)
    conversationEditor.grid(row=1, column=0)

    conversationView = uibuilder.createList(conversationEditor, "Conversations", ["Pest Control"])
    conversationView.grid(row=0, column=0)

    conversationForm = stellarisuibuilder.createConversationForm(conversationEditor)
    conversationForm.grid(row=0, column=1)

    root.mainloop()
