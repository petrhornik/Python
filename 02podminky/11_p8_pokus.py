a = int(input("Zadej délku 1. odvěsny:"))
b = int(input("Zadej délku 2. odvěsny:"))
if(a > 0) and (b > 0):
    c = a**2 + b**2 # dalo by se i napsat (a**2 + b**2) * (1/2)
    print("Přepona trojúhelníku má délku", c * (1/2)) # dá se i použít ** (1/2) protože ** se dá použít i pro odmocniny
else:
    print("Trojúhelník nemůže mít nulovou délku strany!")
