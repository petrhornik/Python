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

# jiné řešení
vek = int(input("kolik ti je? "))
if vek >= 110:
    print("Neplatný vstup")
elif vek >=18:
    # tahle větev se např.: pro "200" už neprovede.
    print("víno, rum, pivo")
elif vek >= 1:
    print("mléko, čas, cola")
elif vek >= 0:
    print("voda")
else:
    # nenastala ani jedna ze situací výše - muselo to být záporné
    print("Neplatný vstup!")