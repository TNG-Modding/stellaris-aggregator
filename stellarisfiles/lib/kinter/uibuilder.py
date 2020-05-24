from tkinter import *

def createPackedLabel(root, labelText):
    label = Label(root, text=labelText, anchor=W, justify=LEFT)
    label.pack()
    return label

def createTextField(root, labelText, height):
    frame = Frame(root)

    label = Label(frame, text=labelText)
    label.grid(row=0, column=0)
    
    textField = Entry(frame, width=30)
    textField.insert(0, labelText)
    textField.grid(row=0, column=1)

    return frame

def createList(root, name, items):
    frame = Frame(root)

    listLabel = createPackedLabel(frame, name)

    listbox = Listbox(frame)
    listbox.pack()

    for item in items:
        listbox.insert(END, item)

    return frame
