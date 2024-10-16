cislo = 0
if (cislo == 0):
    cislo = 1
if (cislo == 1):
    cislo = 0
print(cislo)

# Na začátku máme v čísle nulu, první podmínka se jistě splní
# a dosadí do čísla jedničku. No ale rázem se splní i ta druhá podmínka
# Když podmínky otočíme, budeme mít stejný problém s jedničkou
# Ven se z toho dostaneme tak, že použijeme else
print()

cislo = 0
if (cislo == 0):
    cislo = 1
else:
    cislo = 0
print(cislo)