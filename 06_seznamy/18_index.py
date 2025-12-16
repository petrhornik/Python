""" všechna čísla v seznami zvětšíme o 1 """

seznam = [1, 2, 3]
for index in range(len(seznam)):
    seznam[index] = seznam[index] + 1
print(seznam)

print()
""" funkce enumerate() vrací index prvku i jeho hodnotu"""
seznam = [5, 9, 3]
for i, prvek in enumerate(seznam):
    print(i, prvek)