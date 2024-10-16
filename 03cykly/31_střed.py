import turtle

turtle.speed(-10000)

for j in range(360):
    for i in range(3):
        turtle.forward(200)
        turtle.left(120)
    turtle.left(1)

turtle.pencolor("red")
turtle.pensize("5")

turtle.distance(0, 0)           # posune kurzor na určitou lokaci (v tomto případě x=0 a y=0, nebo-li na střed)

for k in range(360):            # Opakovač nastaven na 360
    turtle.circle(10)            # Velikost jedné kružnice - udává poloměr velkého kruhu
    turtle.left(1)              # Posun o 1px
                                # všech 360 kružnic se nám spojí do sebe a stane se z nich jeden velkej kruh který
                                # vyznačuje střed
turtle.exitonclick()