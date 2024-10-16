""" Řazení
    metoda sort - která prvky v seznamu seřadí """

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort()
print(seznam)
print()

"""Metoda sort zná pojmenovaný argument reverse
    pokud ho nastavím na True, řadí se naopak"""

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort(reverse=True)
print(seznam)