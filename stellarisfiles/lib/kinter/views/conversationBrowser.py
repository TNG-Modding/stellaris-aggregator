
class ConversationForm:
    def __init__(self, parent):
        self.frame = Frame(parent)
        self.parent = parent

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