# Zde jsme použili znakový řetězec: už víme, že znakový řetězec je plastně posloupnost znaků

for pismeno in "Python":
    print(pismeno * 10, end=" * ")

print("\n")

# stejný výsledek bychom dosáhli i tímto zápisem for-cyklu:

for pismeno in "P", "y", "t", "h", "o", "n":
    print(pismeno * 10, end=" * ")