from tkinter import *

class PackedLabel(Label):
    def __init__(self, parent, labelText):
        Label.__init__(self, parent, text=labelText, anchor='nw')
        self.pack(fill='both')
    def updateText(self, text):
        self["text"] = text

class FixedWidthLabel(Frame):
    def __init__(self, parent, labelText, w, h):
        Frame.__init__(self, parent, width=w, height=h)
        self.label = Label(self, text=labelText, anchor='nw')
        self.label.pack(fill="both", expand=1)

    def updateText(self, text):
        self.label["text"] = text

class PackedFieldTextField(Frame):
    def __init__(self, parent, labelText, height):
        Frame.__init__(self, parent)

        self.FieldLabel = Label(frame, text=labelText, anchor='nw')
        self.FieldLabel.grid(row=0, column=0)
        
        self.TextField = Entry(frame, width=30, anchor='nw')
        self.TextField.insert(0, labelText)
        self.TextField.grid(row=0, column=1)

class PackedList(Frame):

    def getListbox(self):
        return self.ListBox

    def replaceListItems(self, items):
        self.ListBox.delete(0,'end')
        for item in items:
            self.ListBox.insert(END, item)

    def __init__(self, parent, name, items, w, h):
        Frame.__init__(self, parent)

        self.Label = PackedLabel(self, name)

        self.ListBox = Listbox(self, width=w, height=h, exportselection=False)
        self.ListBox.pack()

        for item in items:
            self.ListBox.insert(END, item)
