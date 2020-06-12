from tkinter import *

class PackedLabel(Label):
    def __init__(self, parent, labelText):
        Label.__init__(self, parent, text=labelText, anchor='nw')
        self.parent = parent
        self.pack(fill='both')
    def updateText(self, text):
        self["text"] = text

class FixedWidthLabel(Frame):
    def __init__(self, parent, labelText, w, h):
        Frame.__init__(self, parent, width=w, height=h)
        self.parent = parent
        self.label = Label(self, text=labelText, anchor='nw')
        self.label.pack(fill="both", expand=1)

    def updateText(self, text):
        self.label["text"] = text

class PackedTextField(Frame):
    def updateText(self, text):
        self.TextField.delete("1.0", "end")
        self.TextField.insert("1.0", text)

    def __init__(self, parent, labelText, height):
        Frame.__init__(self, parent)
        self.parent = parent
        self.FieldLabel = Label(self, text=labelText)
        self.FieldLabel.grid(row=0, column=0)
        
        self.TextField = Text(self, width=60, height=height)
        self.TextField.grid(row=1, column=0)

class PackedEntryField(Frame):
    def updateText(self, text):
        self.TextField.delete(0, "end")
        self.TextField.insert(0, text)

    def __init__(self, parent, labelText):
        Frame.__init__(self, parent)
        self.parent = parent
        self.FieldLabel = Label(self, text=labelText)
        self.FieldLabel.grid(row=0, column=0)
        
        self.TextField = Entry(self, width=60)
        self.TextField.grid(row=1, column=0)

class PackedButton(Button):
    def __init__(self, parent, text, *args, **kwargs):
        Button.__init__(self, parent, text=text, highlightbackground='#3E4149', *args, **kwargs)
        self.parent = parent
        self.pack()

class PackedList(Frame):

    def getListbox(self):
        return self.ListBox

    def getCurrentlySelected(self):
        if self.ListBox.curselection() == ():
            return None
        return (self.ListBox.curselection()[0], self.ListBox.get(self.ListBox.curselection()))

    def replaceListItems(self, items):
        self.ListBox.delete(0,'end')
        for item in items:
            self.ListBox.insert(END, item)

    def __init__(self, parent, name, items, w, h):
        Frame.__init__(self, parent)
        self.parent = parent

        self.Label = PackedLabel(self, name)

        self.ListBox = Listbox(self, width=w, height=h, exportselection=False)
        self.ListBox.pack()

        for item in items:
            self.ListBox.insert(END, item)
