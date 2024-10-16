#tělo funkce může mít více příkazů. včetně podmínek, cyklů a podobně

def napis_hlasku(nazev, skore):
    "Popíše skóre. Název má být přivnastňovací přídavné jm."
    print(nazev, "skóre je:", skore)
    if skore > 1000:
        print("Světový rekord!")
    elif skore > 100:
        print("Skvělé!")
    elif skore > 10:
        print("Ucházející.")
    elif skore > 1:
        print("Aspoň něco.")
    else:
        print("Snad příště.")

napis_hlasku("Tvoje", 256)
napis_hlasku("Protivníkovo", 5)