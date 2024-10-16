from math import pi

a = float(input("Zadej dělku poloosy 1: "))
b = float(input("Zadej dělku poloosy 2: "))

def obsah_elipsy(a, b):
    "Vrátí obsah elipsy s poloosami danýchg délek"
    # Jen samotný výpočet
    return pi * a * b

#print a input jsou "venku"

print("Obsah je", obsah_elipsy(a, b))