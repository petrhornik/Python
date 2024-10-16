# další přiklad ilustruje for-cyklus, ve kterém počet průchodů určuje načtena hodnota nějaké proměnné:

n = int(input("Zadej počet: "))
for i in range(1, n + 1):
    print('*' * i)

# Program vypíše n řádků, přičemž v prvním je jedna hvězdička, ve druhém je počet n