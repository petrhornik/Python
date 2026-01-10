prvocisla = [2, 3, 5, 7, 11, 13, 17]
print(prvocisla)
prvocisla.append(19) # .append přidá dannou věc do funkce vždy na konec. .append nic nevraci (vraci tzv.None), ale
print(prvocisla)     # "na místě" (Place v ang.) změní seznam, na kterém pracuje

"""Takové měnění hodnoty může být občas překvapující, protože stejnou hodnotu může mít ve více proměnných.
    Protože se mění hodnota samotná, může to vypadat, že se proměnná "mění aniž na ni sáhneme"            """

a = [1, 2, 3]   # vytvoření setnamu
b = a           # tady se nový seznam nevytváří

# seznam vytvořený v 1. řádku má teď 2 jména:
# "a" a "b"
# ale stále pracujeme jenom s jedním seznamem

print(b)
a.append(4)
print(b)