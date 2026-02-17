pocet = int(input("Koncová vzdálenost bodu:"))

kroky = 0
for i in range(1, pocet + 1):
    print("Krok cyklu:", i)
    if i % 2 != 0:
        kroky += 15
        print("Zde není rovina!")
    else:
        print("Koza popošla o 10 kroků!")
        kroky +=10
    if kroky > 50:
        print("Koza skočila na začátek!")
        kroky = 0
    print("pozice kozy:", kroky)

print("Koza je v cíli!")
print(kroky)
