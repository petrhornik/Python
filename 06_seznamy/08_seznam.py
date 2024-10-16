"""Další mazací metody jsou:
    pop - která odstraní a vrátí poslední prvek v seznamu - např. pokud mám seznam karet v balíčku, jde takhle jednoduše
            (líznout) kartu
    remove - která najdev seznamu daný prvek a odstraní ho
    clear - která vyprázdní celý seznam"""

cisla = [1, 2, 3, "abc", 4, 5, 6, 12]
posledni = cisla.pop()
print(posledni)
print(cisla)

cisla.remove("abc")
print(cisla)

cisla.clear()
print(cisla)