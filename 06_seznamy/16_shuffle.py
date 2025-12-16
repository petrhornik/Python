""" Modul random obsahuje 2 funkce, které se hodí k seznamům.
    Jako random.randrange, obě mají něco společného s náhodou.
    Funkce shuffle seznam "zamíchá" - všechny prvky náhodně přehází.
     Funkce shuffle nic nevrací."""

import random

balicek = []
for barva in "zelene", "červene", "žaludy", "koule":
    for hodnota in list(range(2,11)) + ["J", "Q", "K", "A"]:
        balicek.append(str(hodnota) + "-" + barva)
print(balicek)

random.shuffle(balicek)
print(len(balicek))
print()
print(balicek)