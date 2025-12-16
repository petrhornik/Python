vysledek_znamek = 0
vsechny_znamky = 0
vsechny_vahy = 0

try:
    pocet = (int(input("Kolik budeš zadávat známek? ")))
    for  i in range(pocet):
        znamka = int(input("Zadej znamku: "))
        vaha = int(input("Zadej vahu: "))
        if 0 < znamka <=5 and 0 < vaha <=10:
            vysledek_znamek = znamka * vaha
            vsechny_vahy = vsechny_vahy + vaha
            vsechny_znamky = vsechny_znamky + vysledek_znamek
        else:
            print("Toto zadání není možné!!!")
            exit()
except ValueError:
    print("Neplatné zadání!")
    exit()


prumer = vsechny_znamky / vsechny_vahy

print("Vazeny prumer techto znamek je: ", prumer)
