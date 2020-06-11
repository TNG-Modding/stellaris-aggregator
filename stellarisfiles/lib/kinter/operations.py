from tkinter import *
from .views.mainApplication import MainApplication

def createWindow(filepaths, conversations, localizations):
    root = Tk()
    MainApplication(root, filepaths, conversations, localizations).pack(side="top", fill="both", expand=True)
    root.mainloop()
