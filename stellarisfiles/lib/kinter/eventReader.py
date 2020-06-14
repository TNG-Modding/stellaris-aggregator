from ..fileloader import operations as fileloader
import os

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

def localizeValue (identifier, localizations):
    if identifier is None:
        return { "id": identifier, "local": None, "isLocalized": False }

    isLocalized = identifier in localizations
    return { "id": identifier, "local": localizations[identifier] if isLocalized else None, "isLocalized": isLocalized }

def getEvents(filepath):
    return fileloader.LoadStellarisFile(filepath)

def getEventName(event, localizations):
    eventTitle = findFirstChild(event, "title")
    eventId = findFirstChild(event, "id")

    if not eventTitle is None and eventTitle in localizations:
        return "%s -- %s" % (eventId, localizations[eventTitle])
    if not eventId is None:
        return "%s" % (eventId)
    
    return "No title"

def getEventDescription(event, localizations):
    eventDesc = findFirstChild(event, "desc")
    if not eventDesc is None:
        if not isinstance(eventDesc, str):
            eventDesc = findFirstChild(eventDesc, "text") 
        return localizations[eventDesc] if eventDesc in localizations else eventDesc
    
    return "No description"

def getEventOptions(event, localizations):
    options = findAllChildren(event, "option")
    eventOptions = []
    for option in options:
        eventOption = {}
        optionId = findFirstChild(option, "name")
        optionTooltip = findFirstChild(option, "custom_tooltip")
        eventOption["id"] = optionId
        eventOption["name"] = localizations[optionId] if optionId in localizations else optionId
        eventOption["tooltip"] = localizations[optionTooltip] if optionTooltip in localizations else optionTooltip
        eventOptions.append(eventOption)
    return eventOptions 

def getEventSummary(event, localizations):
    eventSummary = {}
    eventContents = event[1]

    eventSummary["id"] = findFirstChild(eventContents, "id")
    eventSummary["name"] = getEventName(eventContents, localizations)
    eventSummary["description"] = getEventDescription(eventContents, localizations)
    eventSummary["options"] = getEventOptions(eventContents, localizations)

    return eventSummary

def getEventIds(events, localizations):
    ids = []
    for event in events["events"]:
        ids.append(getEventSummary(event,localizations)["name"])
    return ids

def getOptionListHeader(options, localizations):
    ids = []
    for option in options:
        optionHeader = option["name"]
        if "tooltip" in option and option["tooltip"] != None:
            if len(option["tooltip"]) >= 30:
                optionHeader += " -- " + option["tooltip"][0:30] + "..."
            else:
                optionHeader += " -- " + option["tooltip"]
            
        ids.append(optionHeader)
    return ids

def getFileNameForFilepath(filepath):
    return os.path.basename(filepath)