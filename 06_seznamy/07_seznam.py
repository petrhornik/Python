"""Mazání prvků
    Přiřazením do podseznamu se dá i změnit délka seznamu, nebo některé prvky úplně odstranit: """

cisla = [1, 2, 3, 4]
cisla[1:-1] = [0, 0, 0, 0, 0, 0]
print(cisla)
cisla[1:-1] = []
print(cisla)
print()

"""Tenhle zápis pro mazání prvků je ale docela nepřehledný, a proto na to máme zvláštní příkaz jménem del.
    Jak už jeho název napovídá, smaže, co mu přijde pod ruku - jednotlivé prvky seznamů, podseznamy a dokonce i
    proměnné !!!!!!!!!  """

cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)
del cisla
print(cisla)