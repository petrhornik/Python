# Napiš program, který nechá uživatele zadávat čísla, dokud jejich součet nedosáhle 100.
A = 0
while True:

    B = int(input("Zadej číslo: "))
    A = A + B

    if A >= 100:
        break
    else:
        print("Číslo je", A, "Zadej další číslo")

print("\n")
print("Číslo je:", A)
print("Tvůj výsledek dosáhl/přesáhl 100.")

if A > 100:
    print("Hodnotu 100 jste přesáhli o:", A - 100)