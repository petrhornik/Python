print("Jednoduchá kalkulačka \n")

# 1. řešení
x = int(input("Zadej první číslo: "))
y = int(input("Zadej druhé číslo: "))
soucet = x + y
rozdil = x - y
soucin = x * y
podil = x / y

print() #také funguje na vynechání řádku (stejně jako \n
print("Součet: ", soucet)
print("Rozdíl: ", rozdil)
print("Součin: ", soucin)
print("Podíl: ", podil)

# 2. řešení
x = int(input("\nZadej první číslo: ")) # to \n tam být nemusí!!!!
y = int(input("Zadej druhé číslo: "))

print("Součet: ", x + y)
print("Rozdíl: ", x - y)
print("Součin: ", x * y)
print("Podíl: ", x / y)
