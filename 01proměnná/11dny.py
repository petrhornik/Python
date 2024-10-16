den = int(input("Jaké je pořadové číslo dne vašeho odjezdu (1-Pondělí, 7-Neděle) "))
delka = int(input("Jaká je délka vašeho pobytu ve dnech "))

print("Pořadové číslo vašeho návratu je", den + delka)
print("Pokud je výsledek nula, jedná se o neděli. Zbytek po dělení 7:", (den + delka) % 7)