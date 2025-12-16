import random

ceny = ["auto", "kolo", "popelnice", "poukaz", "vino", "pivo"]
lide = ["Adam", "Božena", "Cecilie"]

for i in range(len(ceny)):
    cena = ceny.pop()                   # pop zajišťuje že se nebude v tomto případě ceny opakovat
    vyherce = random.choice(lide)
    print(cena, "vyhrává", vyherce)