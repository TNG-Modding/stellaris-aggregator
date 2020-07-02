from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
from pprint import pprint
import json

def HandleXmlChildren(parentElement, child):
    if isinstance(child, list):
        for grandchild in child:
            HandleXmlChildren(parentElement, grandchild)
    elif isinstance(child, tuple):
        childElement = SubElement(parentElement, child[0])
        HandleXmlChildren(childElement, child[1])
    else:
        parentElement.text = child
    
def ConvertParsedObjectToXml (parsed):
    eventElement = Element("events")
    for event in parsed["events"]:
        HandleXmlChildren(eventElement, event)
    return tostring(eventElement)


manyKeys = {
    "country_event": "events",#"country_events",
    "ship_event": "events",#"ship_events",
    "fleet_event": "events",#"fleet_events",
    "planet_event": "events",#"planet_events",
    "event": "events",
    "option": "options",
    "custom_tooltip": "custom_tooltips",
    "trigger": "triggers",
    "name": "names",
    "event_chain": "event_chains",
    "targets": "target",
    "begin_event_chain": "begin_event_chain",
    "event_chain": "begin_event_chains",
    "immediate": "immediate",
    "show_sound": "show_sounds",
    "picture": "pictures",
    "title": "titles",
    "desc": "descriptions",
    "id": "ids",
    "if": "ifs",
    "limit": "limits",
    "NOT": "NOTS",
    "OR": "ORS",
    "AND": "ANDS",
    "NOR": "NORS",
    "remove_country_flag": "country_flag_removes",
    "has_country_flag": "has_country_flags",
    "set_global_flag": "set_global_flags",
    "factor": "factors",
    "modifier": "modifiers",
    "has_civic": "has_civics",
    "has_authority": "has_authorities"
}

duplicate_keys = []

def AssignValueToJson(parent, key, child, seperator):
    if key in manyKeys:
        key = manyKeys[key]

        if key in parent:
            parent[key].append(child)
        else:
            parent[key] = [child]
    else:
        if key in parent:
            if isinstance(parent[key], list):
                parent[key].append(child)
            else:
                newlist = [parent[key], child]
                parent[key] = newlist
        else:
            parent[key] = child

indentor = "    "

def AssignObjectFromList(parent, objectName, children, level):
    seperator = indentor * level
    # print(seperator, "Creating new item to handle item children")
    # print(seperator, "--")
    listItem = {}
    for child in children:
        # print(seperator, "Adding child to parent", parent)
        # print(seperator, "Attempting to add child", child)
        AssignTupleToItem(listItem, child, level+1)
    AssignValueToJson(parent, objectName, listItem, seperator) 

def AssignTupleToItem(parent, pair, level):
    seperator = indentor * level
    if isinstance(pair[1], tuple):
        newObject = {}
        AssignTupleToItem(newObject, pair[1], level+1)
        AssignValueToJson(parent, pair[0], newObject, seperator)
    elif isinstance(pair[1], list):
        objectName = pair[0]
        children = pair[1]
        AssignObjectFromList(parent, objectName, children, level+1)
    else:
        AssignValueToJson(parent, pair[0], pair[1], seperator)

def ConvertParsedToJson (parsed, filenameNoExtension):
    # pprint(parsed)
    validJson = {}
    try:
        AssignObjectFromList(validJson, "file", parsed["events"], 0)
    except Exception:
        import traceback
        traceback.print_exc(limit=2)
    
    return validJson