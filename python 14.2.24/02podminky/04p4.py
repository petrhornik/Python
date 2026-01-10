cislo = int(input("Zadej nějaké číslo, ze kterého spočítam odmocninu: "))
if (cislo > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit!")
    odmocnina = round(cislo * (1/2), 2)
    print("Odmocnina z čísla", cislo, "je", odmocnina)
if (cislo <= 0):
    print("Odmocnina ze záporného čísla a nuly neexistuje!")
print("Děkuji za zadání")

print()

cislo = int(input("Zadej nějaké číslo, ze kterého spočítam odmocninu: "))
if (cislo > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit!")
    odmocnina = round(cislo * (1/2), 2)
    print("Odmocnina z čísla", cislo, "je", odmocnina)
else:
    print("Odmocnina ze záporného čísla a nuly neexistuje!")
print("Děkuji za zadání")

# Rozdíl mezi dvěma if-y a if + else:
# 2 if-y za sebou: Postupně od prvního if-u provede test podmínek
# a vždy se podívá u if-u na podmínku a buď ji splní nebo ne
# (Buď je True nebo False)

# if + else: Podívá se na podmínku u if-u, vyhodnotí True nebo False
# a v případě True vykoná blok if. Pokud je to False, vykoná se blok else
# Kod je mnohem přehlednější a nemusíme vymýšlet opačnou podmínku
