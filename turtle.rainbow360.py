# Codes by Recca Sales
# Written for educational purposes of the author.
# 1/22/2022
import random
from turtle import *
rainbow = ("red","orange","yellow","green", "blue","violet",)
speed(15)
pensize(6)
Screen().bgcolor("black")
hideturtle()
def
def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)
def snowflakeArm():
    for x in range (0,4):
        forward(30)
        vshape()
    backward(120)
def snowflake():
    for x in range(0,15):
        color(random.choice(rainbow))
        snowflakeArm()
        right(24)
snowflake()
mainloop()
