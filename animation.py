from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    t = Turtle()
    t.penup()
    t.pencolor("black")
    t.speed(0)
    t.begin_fill()
    t.goto(-235,235)
    t.pendown()
    for i in range(4):
        t.forward(460)
        t.right(90)
    t.end_fill()
    
def move_forward(turtle):
    turtle.forward(5)

    if turtle.xcor() > 220 or turtle.xcor() < -225:
        turtle.speed(0)
        turtle.setheading(180 - turtle.heading())
        turtle.speed(5)
    if turtle.ycor() > 225 or turtle.ycor() < -225:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
    turtle.speed(5)

def move_xy(turtle, deltaX, deltaY):
    newX = turtle.xcor() + deltaX
    newY = turtle.ycor() + deltaY

    if newX > 220 or newX < -230:
        deltaX *= -1
        newX = turtle.xcor()
    if  newY > 230 or newY < -225:
        deltaY *= -1
        newY = turtle.ycor()
    turtle.goto(newX, newY)
    return deltaX, deltaY
screen = Screen()
screen.bgcolor("white")
screen.setup(500,500)
shape = Turtle()
shape.shape("circle")
shape.color(generate_color())
shape.speed(10)
deltaX = random.randint(-5,5)
deltaY = random.randint(-5,5)

playing_area()

while True:
    deltaX, deltaY = move_xy(shape, deltaX, deltaY)

screen.exitonclick()