# lokální a globální proměnné
    #funkce může používat proměnné "zvnějšku"

pi = 3.1415926

def obsah_kruhu(polomer):
    return pi * polomer ** 2

print(obsah_kruhu(100))

import turtle

for i in range (20):
    turtle.circle(50)
    turtle.left(150)
turtle.exitonclick()