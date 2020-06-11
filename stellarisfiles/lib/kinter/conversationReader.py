def getConversationListHeaders(conversations):
    conversationListHeaders = []
    for conversation in conversations:
        conversationListHeaders.append(conversation["name"])

    return conversationListHeaders