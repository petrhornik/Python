""" Když chci n-tici předat do funkce, narazím na problém, že čárka odděluje jednotlivé argumenty funkce.
    V piodobných připadech musím n-tici uzavřít do závorek, aby bylo jasné, že jde o jednu hodnotu(byť složenou) :) """

seznam_dvojic = []
for i in range(10):
    #   'append' bere jen jeden argument, dáme mu jednu dvojici
    seznam_dvojic.append((i, i**2))
print(seznam_dvojic)