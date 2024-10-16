# vypsání sudých čísel do zadaného počtu (maxima):

max = int(input("Zadej jakékoli celé číslo: "))
cislo = 1
while cislo <= max:
        if cislo % 2 == 0:      # číslo je sudé
            print(cislo)
        cislo = cislo + 1

# tip: break = vyskočení z cyklu, continue == na začátek bloku příkazů