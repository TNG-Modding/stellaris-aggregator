from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

import numbers
import decimal

def HandleChildren(parentElement, child):
    if isinstance(child, list):
        for grandchild in child:
            HandleChildren(parentElement, grandchild)
    
    elif isinstance(child, tuple):
        childElement = SubElement(parentElement, child[0])
        HandleChildren(childElement, child[1])

    else:#if isinstance(child, numbers.Number) or isinstance(child, decimal) or isinstance(child, str):
        parentElement.text = child
        print("Created subelement", child)
    
def ConvertParsedObjectToXml (parsed):
    eventElement = Element("events")
    for event in parsed["events"]:
        HandleChildren(eventElement, event)
    return tostring(eventElement)