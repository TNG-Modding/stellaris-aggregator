def findFirstChild(eventContents, key):
    for keyValue in eventContents:
        if keyValue[0] == key:
            return keyValue[1]
    return None

def findAllChildren(eventContents, key):
    children = []
    for keyValue in eventContents:
        if keyValue[0] == key:
            children.append(keyValue[1])
    return children

def getEventName(event, localisations):
    eventTitle = findFirstChild(event, "title")
    eventId = findFirstChild(event, "id")

    if not eventTitle is None and eventTitle in localisations:
        return "%s -- %s" % (eventId, localisations[eventTitle])
    if not eventId is None:
        return "%s" % (eventId)
    
    return "No title"

def getEventDescription(event, localisations):
    eventDesc = findFirstChild(event, "desc")
    if not eventDesc is None:
        if not isinstance(eventDesc, str):
            eventDesc = findFirstChild(eventDesc, "text")         
        return localisations[eventDesc] if eventDesc in localisations else eventDesc
    
    return "No description"

def getEventOptions(event, localisations):
    return findAllChildren(event, "option")

def getEventSummary(event, localisations):
    eventSummary = {}
    eventContents = event[1]
    
    eventSummary["name"] = getEventName(eventContents, localisations)
    eventSummary["description"] = getEventDescription(eventContents, localisations)
    eventSummary["options"] = getEventOptions(event, localisations)

    return eventSummary

def getEventIds(events, localisations):
    ids = []
    for event in events["events"]:
        pprint(even)
        eventTitle = findFirstChild(event, "title")
        eventId = findFirstChild(event, "id")

        if not eventTitle is None and eventTitle in localisations:
            ids.append("%s -- %s" % (eventId, localisations[eventTitle]))
        if not eventId is None:
            ids.append("%s" % (eventId))
    return ids