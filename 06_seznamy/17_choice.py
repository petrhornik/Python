""" Funkce choice() ze seznamu vybere jeden náhodný prvek """

import random

mozne_tahy = ["Kámen", "Papír", "Nůžky"]
for i in range(10):
    tah_pocitace = random.choice(mozne_tahy)
    print(tah_pocitace)


""" Funkce copy() kopíruje seznam """

lide = ["Adam", "BOB", "Cirda", "Dana", "Eva", "gusťa"]
kopie = lide.copy()
print(lide)
print(kopie)