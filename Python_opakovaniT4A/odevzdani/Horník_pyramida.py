a = int(input("Zadej výšku pyramidy: "))

for i in range(a):
    print(" " * (a - i), end="") # end="" -> určí, že se bude pokračovat na stejném řádku
    print("X" * (i + 1) + "X" * i)


