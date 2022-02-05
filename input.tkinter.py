from tkinter import Entry

from future.moves import tkinter
from tkinter import *

#root = window

root = Tk()

e = Entry(root, width = 50, borderwidth=5)
e.pack()


def myClick():
    myLabel = Label(root, text = "Hello, " + e.get())
    myLabel.pack()

#fg = foreground, bg = background
myButton = Button(root, text= "Enter your name.", command = myClick)

myButton.pack()

root.mainloop()
