import turtle
turtle.pencolor("green")        # Barva pera.
turtle.pensize("20")             # Velikost pera.
turtle.bgcolor("black")         # Barva pozadí.

turtle.shape("turtle")      # Tento řádek je zbytečný pouze nám změní kreslící "kurzor" na želvu.

for i in range(3):              # Toto nakreslí trojúhelník.
    turtle.forward(100)
    turtle.left(120)
turtle.exitonclick()