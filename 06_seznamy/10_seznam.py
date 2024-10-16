"""Operace se seznamy
    sčítání a násobení číslem"""

melodie = ["C", "E", "G"] * 2 + ["E", "E", "D", "E", "F", "D"] * 2 + ["E", "D", "C"]
print(melodie)
print()

"""Stejně jako u řetězců, sčítat jde jen seznam se seznamem - NE seznam s řetězcem!!
    Další starší známí jsou finkce len, metody count, index a operátor in."""

print(len(melodie))             # délka seznamu
print(melodie.count("D"))       # počet "D" v seznamu
print(melodie.index("D"))       # číslo prvního "D"
print("D" in melodie)           # Je "D" v seznamu?

"""Poslední 3 se ale přece jen chovají kapku jinak:
    u řetězců pracují s podřetězci, u seznamů jen s jednotlivými prvky.
    Takže ačkoliv naše melodie obsahuje prvky "D" a "E" velde sobo, "DE" v seznam není."""

print("DE" in melodie)
print(melodie.count("DE"))
print(melodie.index("DE"))