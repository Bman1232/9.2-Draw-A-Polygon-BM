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
    
def move_forward(turtle, turtles):
    turtle.forward(5)
    if turtle.xcor() > 220 or turtle.xcor() < -225:
        turtle.speed(0)
        turtle.setheading(180 - turtle.heading())
        turtle.speed(5)
        turtles.append(create_turtle())
    if turtle.ycor() > 225 or turtle.ycor() < -225:
        turtle.speed(0)
        turtle.setheading(-turtle.heading())
        turtle.speed(5)
        turtles.append(create_turtle())
    return turtles

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

def create_turtle():
    shape1 = Turtle()
    shape1.speed(0)
    shape1.color(generate_color())
    shape1.shape("circle")
    shape1.seth(random.randint(0,360))
    return shape1
#Setup
screen = Screen()
screen.bgcolor("white")
screen.setup(500,500)
shape = Turtle()
shape.shape("circle")
shape.color(generate_color())
shape.speed(10)
turtles = [shape]

playing_area()

while True:
    for obj in turtles:
        turtles = move_forward(obj, turtles)
    print(turtles)

screen.exitonclick()