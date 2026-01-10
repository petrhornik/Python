import turtle
import random

turtle.colormode(255)
turtle.pensize(5)

for j in range(6):
    for i in range(6):
        for b in range(10):
            turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            turtle.forward(10)
        turtle.left(60)
    turtle.penup()          #Zvedne pero při přesunu už nad nakreslenou vrstvou
    turtle.forward(100)
    turtle.right(60)
    turtle.pendown()        #Položí pero dolů a pokračuje v kreslení

turtle.exitonclick()