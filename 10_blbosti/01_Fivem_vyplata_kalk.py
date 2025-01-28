rozhodovac = 0
print("Program na výpočet výplaty pohodáři!")

while True:
    if rozhodovac == 1:
        break
    celkova_castka = 0
    try:
        celkova_castka = int(input("\nZadej celkovou castku: "))
        celkova_castka = (celkova_castka - (celkova_castka / 160 * 111)) / 2
        print("Celkova castka je: ", round(celkova_castka, 2))
    except ValueError:
        print("Pro funkčnost zadej pouze přirozené číslo!")
    while True:
        try:
            a = int(input("\nPřeješ si počítat znovu? 1-ANO 2-NE\n: "))
            if a == 1:
                rozhodovac = 0
                break
            if a == 2:
                rozhodovac = 1
                break
            else:
                print("Nerozumím zkus to znovu!")
        except ValueError:
            print("Nerozumím zkus to znovu!")

print("\n Zavírám program :D")