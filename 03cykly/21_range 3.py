# for-cyklus se výborně využíje v případech, kdy se v těle cyklu vyskytuje příkaz, který.......

n = int(input("Zadej počet: "))
soucet = 0
for i in range(1, n + 1):
    soucet = soucet + i
print("soucet cisel =", soucet)

# V tomto programu jsme použili proměnnou soucet, do které postupně připočítáváme všechny hodnoty z intervalu (range)
# od 1 do n. Díky tomu se po skončení cyklu v této proměnné nachází právě součet všech celých čísel do n.