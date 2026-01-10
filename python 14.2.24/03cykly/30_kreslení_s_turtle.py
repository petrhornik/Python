import turtle

turtle.speed(-100)          # Rychlost turtle - čím menší tím rychlejší

for j in range(100):
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.left(5)
turtle.exitonclick()
