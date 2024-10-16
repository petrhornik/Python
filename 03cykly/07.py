# Náhoda

# Ukážeme si dvě funkce z modulu random, které jsou velice užitečné pro hry.

from random import randrange, uniform

randrange(a, b) # náhodné celé číslo od a do b-1
uniform(a, b)   # náhodné reálné číslo od a do b
randint(a, b)   # generuje náhodná čísla od a do b (včetně a, b)

# Protože jednotlivé složky barvy jsou čísla v rozmezí 0-255, používáme random.randint(0, 255)
# Pozor na to, že randrange(a, b) nikdy nevrátí samotné b. Pokud potřebujeme náhodně vybrat ze tří možností.