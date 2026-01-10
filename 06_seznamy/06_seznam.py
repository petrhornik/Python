"""Seznamům se dají i měnit jednotlivé prvky a  to jednoduše tak, že do prvku přiřadíme, jako by to byla proměnná: """

cisla = [1, 0, 3, 4]
cisla[1] = 2
print(cisla)

"""Přiřazovat se dá i do podseznamu - v tomto případě se podseznam nahradí jednotlivými prvky toho, co přiřazujeme.
    Jako u .extend můžeš do podseznamu opět přiřadit cokoli, co umí zpracovat for - seznam, řetězec, range() apod. """

cisla =[1, 2, 3, 4]
cisla[1:-1] = [6, 5]
print(cisla) 