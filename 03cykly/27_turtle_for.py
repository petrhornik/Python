import turtle

x = int(input("Zadej počet schodů: "))
y = int(input("Zadej veliokost jednotlivých schodů: "))
for i in range(x):
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(y)
    turtle.right(90)