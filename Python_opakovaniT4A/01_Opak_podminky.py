# podminky - určuje pravdu/nepravdu pomocí if a else

x = int(input("Zadej číslo X: "))
y = int(input("Zadej číslo Y: "))
z = int(input("Zadej číslo Z: "))

# každé číslo sudé, každé číslo větší než 2, max jakéhokoli menší nebo rovno 100
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0 and (x > 2 or y > 2 or z > 2) and max(x,y,z) <= 100:
    print("Vládnou sudáci!")

# alespoň 2 čísla lichá, součet všech je dělitelný 3, max jakéhokoli je menší či roven 100
elif (x % 2 != 0 and y % 2) or (y % 2 != 0 and z % 2 != 0) or (z % 2 != 0 and x % 2 != 0) and (x + y + z) % 3 == 0 and max(x,y,z) <= 100:
    print("Vládnou lichouni!")

# max jakéhokoli čísla je větší než 100, žádné číslo není záporné
elif max(x, y, z) > 100 and x >= 0 and y >= 0 and z >= 0:
    print("Velikani")

# neplatí ani 1 podmínka
else:
    print("vládne mínus")