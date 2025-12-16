vek = int(input("Zadej svůj věk: "))
a = "Nápojový lístek: "

if vek > -1 and vek < 100:
    if vek == 0:
        print(a + "voda")
    elif vek > 0 and vek < 18:
        print(a + "voda, cola, džus, fanta")
    else:
         print(a + "voda, cola, džus, fanta, vodka, rum, pivo")
else:
    print("Neplatný vstup!")