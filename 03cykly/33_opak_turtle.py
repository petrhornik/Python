import turtle

a = int(input("Zadej velikost strany: "))

turtle.fillcolor("red")
turtle.begin_fill()

turtle.pencolor("blue")

for i in range(6):
    turtle.forward(a)
    turtle.left(60)

turtle.end_fill()
turtle.exitonclick()