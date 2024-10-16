n = int(input("Zadej počet: "))
soucin = 1
for i in range(1, n + 1):
    soucet = soucin * i                     # nebo soucin *= i
print("{}! = {}".format(n, soucin))

# výpočetv faktorialu, což je vlastně součin čísel 1 * 2 * 3 * ... * n.
# Pomocná proměnná musí být inicializována 1, namísto přičítání bude násobení.