import turtle
import random

turtle.pensize(10)

def petiuhelnik():
    turtle.pencolor("yellow")
    for i in range(5):
        turtle.left(72)
        turtle.forward(20)

def osmiuhelnik():
    turtle.colormode(255)
    for i in range(8):
        turtle.left(45)
        for i in range(6):
            turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            turtle.forward(10)

def kytka():
    turtle.tracer(0)
    for i in range(30):
        osmiuhelnik()
        turtle.left(20)
    turtle.goto(0, 0)
    for i in range(360):
        petiuhelnik()
        turtle.left(1)

kytka()
turtle.exitonclick()
