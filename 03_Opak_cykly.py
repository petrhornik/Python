# ukázka cyklu for + podminky
# ve for se řasto používá in range()
    # pokud 1 číslo v () -> začne v 0 a opakuje než dojde do čísla
    # -||- 2 čísla -||- -> rozsah od, do
    # -||- 3 čísla -||- -> rozsah od, do, o kolik se posune (4, 11, 2)

pocet = int(input("Kolikrát chceš zamíchat? "))
vysledek = 0
for i in range(1, pocet + 1):
    if i % 2 != 0 and i % 7 != 0:
        print("Míchání", i, "úspěšné")
        vysledek += 1
    else:
        print("Míchání", i, "BUM! Explodovalo ti to!")

print("\nLektvar se povedlo namíchat", vysledek, "krát!")