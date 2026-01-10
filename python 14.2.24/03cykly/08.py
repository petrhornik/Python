import random
cislo = random.randrange(0, 3)

if cislo == 0:
    print("kolečko")
elif cislo == 1:
    print("Čtvereček")
else:   # 2
    print("Trojúhelníček")

# Pamatuj, když importuješ z modulu random, nesmí se tvůj soubor jmenovat random.py