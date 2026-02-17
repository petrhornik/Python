import turtle

move = -30
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 != 0:
                turtle.begin_fill()
        else:
            if j % 2 == 0:
                turtle.begin_fill()
        for k in range(4):
            turtle.forward(30)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(30)
    turtle.setx(0)
    turtle.sety(move)
    move -= 30
turtle.exitonclick()

