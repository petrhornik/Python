x = int(input("Zadej limit:")) # cyklus for pro procházení čísel od 1 do limit (včetně).

for i in range(1, x + 1):
    if i % 2 == 0:              # Podmínka pro kontrolu, zda je číslo sudé.
        print("Sudé číslo je", i)

