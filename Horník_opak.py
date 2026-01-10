# podminky - určuje pravdu/nepravdu pomocí if a else

x = int(input("Zadej číslo X: "))
y = int(input("Zadej číslo Y: "))
z = int(input("Zadej číslo Z: "))


if x > 0 and y > 0 and z > 0:
    if x < z and x < z:
        if z > 100:
            print("Vládnou velikáni!")
    elif x > y and x > z:
        if x > 100:
            print("Vládnou velikáni!")
    elif x < y and z < y:
        if y > 100:
            print("Vládnou velikáni!")
else:

    if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
        if x > 2 or y > 2 or z > 2:
            print("Vládnou sudáci!")


        elif x % 2 != 0 and y % 2 or y % 2 != 0 and z % 2 != 0 or z % 2 != 0 and x % 2 != 0:
            if (x + y + z) % 3 == 0:
                print("Vládnou lichouni!")
            else:
                print("Vládne Pan Mínus!")
        else:
            print("Vládne Pan Mínus!")

