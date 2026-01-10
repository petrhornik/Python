cislo = int(input("Zadejte číslo dne v týdnu: "))
if(cislo > 0 and cislo < 8 ):
    if(cislo == 1):
        print("pondělí")
    elif(cislo == 2):
        print("úterý")
    elif (cislo == 3):
        print("středa")
    elif (cislo == 4):
        print("čtvrtek")
    elif (cislo == 5):
        print("pátek")
    elif (cislo == 6):
        print("sobota")
    elif (cislo == 7):
        print("neděle")
else:
    print("Neplatný vstup!")

mesic = int(input("Zadej číslo měsíce v roce: "))
if(mesic == 12 or mesic < 3 and mesic > 0):
    print("zima")
elif(mesic >= 3 and mesic <= 5):
    print("Jaro")
elif(mesic > 5 and mesic <=8):
    print("léto")
elif(mesic >= 9 and mesic <= 11):
    print("podzim")
else:
    print("neplatný vstup")

if(mesic > 8 and mesic < 13 or mesic == 1):
    print("1. pololetí")
elif(mesic >= 2 and mesic < 7):
    print("2. pololetí")
else:
    print("Nejde!")