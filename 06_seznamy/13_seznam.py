"""Další zp. jak vytvořit seznam je nejdřív udělat prázdný seznam a pomocí .append do něj hodnoty přidávat."""

mocniny_dvou = []
for cislo in range(10):
    mocniny_dvou.append(2 ** cislo)
print(mocniny_dvou)
print()

"""Chceš-li seznam, který reprezentuje balíček karet, zavolej append pro všechny kombinace barev a hodnot."""

balicek = []
for barva in "listy", "srdce", "káry", "piky":
    for hodnota in list(range(2, 11)) + ["J", "Q", "K", "A"]:
        balicek.append(str(hodnota) + "-" + barva)
print(len(balicek))
print(balicek)