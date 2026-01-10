import turtle

turtle.pensize(5)
turtle.speed(0.00002)
turtle.bgcolor("lightblue")

turtle.pencolor("yellow")
for i in range(360):
    turtle.circle(30)
    turtle.left(1)

turtle.setx(0)
turtle.sety(0)

for j in range(30):
    turtle.forward(150)
    turtle.back(150)
    turtle.left(20)

turtle.exitonclick()