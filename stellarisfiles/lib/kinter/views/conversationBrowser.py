from tkinter import *
from .modules import *
from .. import conversationReader
class ConversationList(PackedList):
    def __init__(self, parent, conversations):
        PackedList.__init__(self, parent, "Conversations", conversations, 50, 38)
        self.parent = parent

class ConversationBrowser(Frame):

    def openConversation(self, e):
        widget = e.widget
        index = widget.curselection()[0]
        conversationId = widget.get(index)
        # print ('You selected conversation', index, conversationId)
        self.conversationForm.loadConversation(self.conversations[index])

    def loadConversations(self, conversations):
        self.conversations = conversations
        self.conversationList.replaceListItems(conversationReader.getConversationListHeaders(conversations))
        
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
    
        self.conversationList = ConversationList(self, [])
        self.conversationList.grid(row=0, column=0)
        self.conversationList.getListbox().bind("<<ListboxSelect>>", self.openConversation)

        self.conversationForm = ConversationForm(self)
        self.conversationForm.grid(row=0, column=1)

class ConversationForm(Frame):
    def loadConversation(self, conversation):
        self.conversationVarnameField.updateText(conversation["varname"])
        self.conversationNameField.updateText(conversation["name"])
        self.conversationDescriptionField.updateText(conversation["desc"])
        self.conversationEthicField.updateText(conversation["ethic"])

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self.eventVarLabel = PackedLabel(self, "anomaly.1000")
        self.conversationVarnameField = PackedEntryField(self, "Varname")
        self.conversationVarnameField.pack()

        self.conversationNameField = PackedEntryField(self, "Name")
        self.conversationNameField.pack()

        self.conversationDescriptionField = PackedTextField(self, "Description", 6)
        self.conversationDescriptionField.pack()

        self.conversationEthicField = PackedEntryField(self, "Ethic")
        self.conversationEthicField.pack()

        self.conversationDemandsField = PackedTextField(self, "Demands", 10)
        self.conversationDemandsField.pack()
