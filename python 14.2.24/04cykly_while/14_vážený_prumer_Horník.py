soucet = 0
a = 1
vaha_done = 0
vahy = 0

while True:
    znamka = int(input("Zadej znamku:"))
    if znamka == 0:
        prumer = soucet / pocet_znamek
        break
    else:
        váha = int(input("Zadej váhu známky:"))
        vaha_all = znamka * váha
        vaha_done = vaha_done + vaha_all
        vahy = vahy + váha
        vahovy_prumer = vaha_done / vahy
        soucet = soucet + znamka
        pocet_znamek = a + 1
        continue
print("Vážený průměr:", vahovy_prumer)