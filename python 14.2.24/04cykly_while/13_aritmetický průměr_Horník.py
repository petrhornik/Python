soucet = 0
a = 1

while True:
    znamka = int(input("Zadej znamku:"))
    soucet = soucet + znamka
    pocet_znamek = a + 1
    prumer = soucet / pocet_znamek
    if znamka == 0:
        break
    else:
        continue
print("Aritmetický průměr známek je:", prumer)

# program pro výpočet aritmetického průměru zadaných známek