from turtle import *
import random

screen = Screen()
screen.bgcolor("teal")

pen = Turtle()
pen.speed(0)

def regular_polygon(pen, sides):
    pen.begin_fill()
    for i in range(sides):
        pen.forward(100/(sides/2))
        pen.right(360/sides)
    pen.end_fill()

while True:
    sides = int(input("How many sides for the polygon: "))
    pen.clear()
    if sides != 4:
        regular_polygon(pen, sides)
    elif sides < 3:
        print("A polygon cannot have less than 3 sides, try again.")
    elif sides == 4:
        

screen.exitonclick()