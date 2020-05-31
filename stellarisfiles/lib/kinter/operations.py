from tkinter import *
from . import uibuilder as uibuilder
from . import stellarisuibuilder as stellarisuibuilder

def createWindow(files, localisations):
    root = Tk()

    conversationView = uibuilder.createList(root, "Conversations", ["Pest Control"])
    conversationView.grid(row=0, column=0)

    eventViewer = stellarisuibuilder.createEventViewer(root, files, localisations)
    eventViewer.grid(row=0, column=1)
    
    # Conversation
    # conversationEditor = Frame(root)
    # conversationEditor.grid(row=1, column=0)

    # conversationForm = stellarisuibuilder.createConversationForm(conversationEditor)
    # conversationForm.grid(row=0, column=1)

    root.mainloop()
