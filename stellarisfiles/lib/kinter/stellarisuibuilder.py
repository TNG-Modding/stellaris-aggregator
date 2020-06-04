from tkinter import *
from . import uibuilder as uibuilder
from .. import fileloader as fileloader 
from . import eventReader as eventReader
from pprint import pprint

def openEvents(e):
    widget = e.widget
    index = widget.curselection()[0]
    value = widget.get(index)
    print ('You selected item', index, value)
    events = fileloader.LoadStellarisFile(value)
    for event in events["events"]:
        if "id" in event:
            print(event["id"])

def createFileList(root, files):
    # for item in files:
    #     listbox.insert(END, item)
    # listbox.bind("<<ListboxSelect>>", openEvents)
    return uibuilder.createList(root, "Files", files, 50, 25)   



