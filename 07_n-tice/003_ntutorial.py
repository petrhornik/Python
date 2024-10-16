""" N-tice se hodí, pokud chceš z funkce vrátit víc než jednu hodnotu.
    Prostě v příkazu return oddělím vrácené hodnoty čárkou.
    Vypadá to, že vracím několik hodnot, ale ve skutečnosti se vrací jen jedna n-tice. """

def podilo_a_zbytek(a, b):
    return a // b, a % b
print(podilo_a_zbytek(10, 5))