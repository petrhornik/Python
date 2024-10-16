cislo = int(input("Zadej nějaké číslo, ze kterého spočítam odmocninu: "))
if (cislo > 0):
    print("Zadal jsi číslo větší než 0, to znamená, že ho mohu odmocnit!")
    odmocnina = round(cislo * (1/2), 2) # round zaokrouhlí na číslo za čárkou
    print("Odmocnina z čísla", cislo, "je", odmocnina)
print("Děkuji za zadáni")
