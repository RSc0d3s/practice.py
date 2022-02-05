from future.moves import tkinter
from tkinter import *

#root = window

root = Tk()

#Creating a label widget

myLabel1 = Label(root, text="Hello World.").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Recca.").grid(row=1, column=0)

#putting it into the screen
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)

root.mainloop()
