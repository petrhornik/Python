zasifrovany_text = ["Praha", " t2ts", "éfgto", "oki Kl", "ldráf", "t45knn", "yHr !", "jdrewer", " hj6kl", ",gk8Rtyně", ".zv tlo se", "Pjhott", "zwfohh", "rík!"]

# dešifruje na bázi sudých a lichých čísel = 1. slovo(0) je sudé - program vezve sudé členy ve slově
#                                           2. slovo(1) je liché - program vezme liché členy ve slově

poradi = 0
text = ""

for slovo in zasifrovany_text:
    if poradi % 2 == 0:             # zbytkové dělení 2. Pokud je č. sudé(má zbytek 0) tak pokračuj jinak ignoruj
        sude_cleny = slovo[::2]
        text = text + sude_cleny
        poradi = poradi + 1
    else:
        liche_cleny = slovo[1::2]
        text = text + liche_cleny
        poradi = poradi + 1

print(text)