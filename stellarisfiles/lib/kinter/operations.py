from tkinter import *
from . import uibuilder as uibuilder
from . import stellarisuibuilder as stellarisuibuilder

def createWindow():
    root = Tk()
    filesFrame = uibuilder.createList(root, "Files", ["file"])
    filesFrame.grid(row=0, column=0)

    eventsFrame = uibuilder.createList(root, "Events", ["file"])
    eventsFrame.grid(row=0, column=1)

    eventView = stellarisuibuilder.createEventView(root)
    eventView.grid(row=0, column=2)

    conversationView = uibuilder.createList(root, "Conversations", ["Pest Control"])
    conversationView.grid(row=1, column=0)

    conversationForm = stellarisuibuilder.createConversationForm(root)
    conversationForm.grid(row=1, column=1)

    root.mainloop()
