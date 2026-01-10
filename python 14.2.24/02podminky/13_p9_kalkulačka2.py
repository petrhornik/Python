x = int(input("Zadej první číslo: "))
y = int(input("Zadej druhé číslo: "))
soucet = x + y
rozdil = x - y
soucin = x * y
podil = x / y

print("Sčítat - 1") # výběr početních operací
print("Odčítat - 2")
print("Násobit - 3")
print("Dělit - 4")

cislo_operace = int(input("Zadejte číslo operace: "))  # toto nám určí operaci výběrem čísla
if(cislo_operace == 1):
    print("Součet: ", soucet)
elif(cislo_operace == 2):
    print("Rozdíl: ", rozdil)
elif(cislo_operace == 3):
    print("Součin: ", soucin)
elif(cislo_operace == 4):
    print("Podíl: ", podil)
else:
    print("ERROR")
