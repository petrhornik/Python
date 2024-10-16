import turtle

a = int(input("Zadej velikost strany: "))

for j in range(6):
    for i in range(6):
        turtle.forward(a)
        turtle.left(60)
    turtle.forward(a)
    turtle.right(60)

turtle.exitonclick()