def dalsi_priklad():
    while True:
        odpoved = input("Přejete si zadat další příklad? ")
        if odpoved == "y":
            return True
        elif odpoved == "n":
            return False

def vypocet(prvni_cislo, druhe_cislo):
    print("1. scitani \n 2. odecitani \n 3. nasobeni \n 4. Deleni")
    cislo_operace = int(input("Vyber: "))
    if cislo_operace == 1:
        print("Jejich součet je:", prvni_cislo + druhe_cislo)
    elif cislo_operace == 2:
        print("Jejich rozdíl je:", prvni_cislo - druhe_cislo)
    elif cislo_operace == 3:
        print("Jejich součin je:", prvni_cislo * druhe_cislo)
    elif cislo_operace == 4:
        if druhe_cislo !=0:
            print("Jejich podíl je:", prvni_cislo / druhe_cislo)
        else:
            print("Nelze dělit nulou!")

def kalkulacka():
    pokracovat = True
    while pokracovat:
        prvni_cislo = int(input("Zadej prvni číslo: "))
        druhe_cislo = int(input("Zadej druhé číslo: "))
        vypocet(prvni_cislo, druhe_cislo)
        if not dalsi_priklad():
            pokracovat = False

kalkulacka()
