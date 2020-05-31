from tkinter import *

def createPackedLabel(root, labelText):
    label = Label(root, text=labelText, anchor='nw')
    label.pack(fill='both')
    return label

def createTextField(root, labelText, height):
    frame = Frame(root)

    label = Label(frame, text=labelText, anchor='nw')
    label.grid(row=0, column=0)
    
    textField = Entry(frame, width=30, anchor='nw')
    textField.insert(0, labelText)
    textField.grid(row=0, column=1)

    return frame

def createList(root, name, items):
    frame = Frame(root)

    listLabel = createPackedLabel(frame, name)

    listbox = Listbox(frame, width=100)
    listbox.pack()

    for item in items:
        listbox.insert(END, item)

    return frame
