import turtle

def mnohouhelnik():
    while True:
        x = int(input("Zadej počet úhlů (více než 2): "))
        if x > 2:
            break
        else:
            print("Zadali jste 2 či méně úhlů, zkuste to prosím znovu.")

    pocet_uhlu = 360 / x

    for i in range(x):
        turtle.forward(100)
        turtle.left(pocet_uhlu)
    turtle.exitonclick()

mnohouhelnik()