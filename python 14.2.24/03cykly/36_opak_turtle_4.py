import turtle, random


turtle.colormode(255)
turtle.pensize(2)
turtle.speed(-1000000)

for p in range(100):
    for j in range(6):
        for b in range(10):
            turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            turtle.forward(10)
            turtle.bgcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.left(60)
    turtle.left(5)
