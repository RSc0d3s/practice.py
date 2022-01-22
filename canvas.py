from future.moves import tkinter
import tkinter
print("Draw by holding the left mouse button and moving your mouse around.")
print("Change your brush color by clicking on one of the colors.")
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=1000, height=500, bg="white")
canvas.pack()
lastX, lastY = 0,0
colour = "black"
def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y
def on_click(event):
    store_position(event)
def on_drag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=colour, width=3)
    store_position(event)
canvas.bind("<Button-1>",on_click)
canvas.bind("<B1-Motion>", on_drag)
red_id = canvas.create_rectangle(10,10, 30, 30, fill="red")
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill="blue")
black_id = canvas.create_rectangle(10, 60, 30, 80, fill="black")
green_id = canvas.create_rectangle(10, 85, 30, 105, fill="green")
pink_id = canvas.create_rectangle(10, 105, 30, 130, fill="pink")
orange_id = canvas.create_rectangle(10, 130, 30, 155, fill="orange")
white_id = canvas.create_rectangle(10, 155, 30, 180, fill="white")
def set_colour_red(event):
    global colour
    colour="red"
def set_colour_blue(event):
    global colour
    colour="blue"
def set_colour_black(event):
    global colour
    colour = "black"
def set_colour_green(event):
    global colour
    colour = "green"
def set_colour_pink(event):
    global colour
    colour = "pink"
def set_colour_orange(event):
    global colour
    colour = "orange"
def set_colour_white(event):
    global colour
    colour = "white"
canvas.tag_bind(red_id, "<Button-1>",set_colour_red)
canvas.tag_bind(blue_id, "<Button-1>",set_colour_blue)
canvas.tag_bind(black_id, "<Button-1>",set_colour_black)
canvas.tag_bind(green_id, "<Button-1>",set_colour_green)
canvas.tag_bind(pink_id, "<Button-1>",set_colour_pink)
canvas.tag_bind(orange_id, "<Button-1>",set_colour_orange)
canvas.tag_bind(white_id, "<Button-1>",set_colour_white)
window.mainloop()
