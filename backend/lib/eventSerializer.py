from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
from pprint import pprint

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
    "country_event": "events",
    "ship_event": "events",
    "fleet_event": "events",
    "planet_event": "events",
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
    # if key in manyKeys:
    #     key = manyKeys

    # if key in parent:
    #     newlist = [parent[key], child]
    #     parent[key] = newlist
    # else:
    print(seperator, "Assiging ", child, " to ", key, " of ", parent)
    print(seperator, "---*")
    parent[key] = child

indentor = "    "

def HandleJsonChildren (parent, key, child, level):
    seperator = indentor * level
    print(seperator, "Begin")
    print(seperator, parent)
    print(seperator, key)
    print(seperator, child)
    print(seperator,"-----")
    if isinstance(child, list):
        print(seperator, "Creating new item to handle list of child")
        print(seperator, "--")
        newItem = {}
        i = 0
        for grandchild in child:
            print(seperator, "Adding grandchild to parent", parent)
            print(seperator, "Attempting to add child", grandchild)
            print(seperator, "-")
            if isinstance(child[1], tuple):
                HandleJsonChildren(newItem, grandchild[0][0], grandchild[1], level+1)
            else:
                HandleJsonChildren(newItem, grandchild[0], grandchild[1], level+1) 
            i = i+1
        AssignValueToJson(parent, key, newItem, seperator) 
    elif isinstance(child, tuple):
        # newItem = {}
        # HandleJsonChildren(newItem, child[0], child[1])
        # AssignValueToJson(parent, key, newItem)
        
        if isinstance(child[1], list):
            print(seperator, "Adding complex tuple to parent", parent)
            print(seperator, "Adding key %s" % child[0])
            print(seperator, "Attempting to add list child", child[1])
            print(seperator, "-")
            HandleJsonChildren(parent, child[0], child[1], level+1)
        if isinstance(child[1], tuple):
            print(seperator, "Adding complex tuple to parent", parent)
            print(seperator, "Adding key %s" % child[0])
            print(seperator, "Attempting to add tuple child", child[1])
            print(seperator, "-")
            newItem = {}
            HandleJsonChildren(newItem, child[1][0], child[1][1], level+1)
            AssignValueToJson(parent, key, newItem, seperator)
        else:
            print(seperator, "Adding simple tuple to parent", parent)
            print(seperator, "Adding key %s" % child[0])
            print(seperator, "Attempting to add child", child[1])
            print(seperator, "-")
            newItem = {}
            AssignValueToJson(parent, child[0], child[1], seperator)
    else:
        print(seperator, "Assigning child", child, " to ", key, " of ", parent)
        print(seperator, "$$$")
        AssignValueToJson(parent, key, child, seperator)

def ConvertParsedToJson (parsed):
    validJson = {}
    HandleJsonChildren(validJson, "file", parsed["events"], 0)
    pprint(validJson)
    return parsed