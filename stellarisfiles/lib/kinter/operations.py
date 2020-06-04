from tkinter import *
from .views.mainApplication import MainApplication

def createWindow(filepaths, localizations):
    root = Tk()
    MainApplication(root, filepaths, localizations).pack(side="top", fill="both", expand=True)
    root.mainloop()
