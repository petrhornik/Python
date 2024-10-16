"""funkce list - převádí na seznam
    Jako argument jí předáme jakoukoli hodnotu, kterou umí zpracovat příkaz for. Z řetězců udělá seznam znaků,
    z otevřeného souboru udělá seznam řádků, z range() udělá seznam čísel"""

abeceda = list("abcdefghijklmnopqrstuvwxyz")
cisla = list(range(100))
print(abeceda)
print(cisla)
print()

"""I zeseznamu udělá funkce list seznam.
    - vytvoří nový seznam
    - stejné prvky, ale není to ten samý seznam
    - funguje nezávisle na tom starém"""

a = [1, 2, 3]
b = list(a)


print(b)
b.append(4)
print(b)
print(a)