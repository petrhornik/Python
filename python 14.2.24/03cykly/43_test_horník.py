for i in range(1, 64):
    a = 2 ** 64 - 1
print("Číslo je: ", a)

# jiné řešení

zrn = 0
policka = 1
for i in range(1, 65):
    zrn = zrn + policka
    policka = policka * 2
print("Číslo je: ",zrn)

