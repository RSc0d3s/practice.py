from future.moves import tkinter
from tkinter import *

#root = window

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look!")
    myLabel.pack()

#fg = foreground, bg = background
myButton = Button(root, text= "Click Me!", padx = 50, pady = 50,
                  command = myClick, fg="blue", bg = "white")

myButton.pack()

root.mainloop()
