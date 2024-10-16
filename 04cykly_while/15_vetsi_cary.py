import turtle

delka = 0
cara = 0

for i in range(25):
    turtle.forward(i)       #Proměnná i se při každém průchodu cyklem zvětší o 1, proto je každá čára o jeden pixel
                            # větší než předchozí
    turtle.penup()
    turtle.forward(2)
    turtle.pendown()
turtle.exitonclick()        #Obě řešení jsou správně, ale jedno z nich se musí vždy "zakomentovat" pomocí # pro
                            # správnou funkčnost
while cara < 20:
    turtle.forward(cara)
    cara = cara + 1
    turtle.penup()
    turtle.forward(2)
    turtle.pendown()
turtle.exitonclick()