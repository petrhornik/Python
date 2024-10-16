# funkce co výsledek vrací lze použít i v dalších výpočtech

from math import pi

def obsah_elipsy(a, b):
    return pi * a * b

def objem_eliptickeho_valce(a, b, vyska):
    return obsah_elipsy(a, b) * vyska

print(objem_eliptickeho_valce(3, 5, 3))