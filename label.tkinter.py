from future.moves import tkinter
from tkinter import *

#root = window

root = Tk()

#Creating a label widget

myLabel = Label(root, text="Hello World.")

#putting it into the screen
myLabel.pack()

root.mainloop()
