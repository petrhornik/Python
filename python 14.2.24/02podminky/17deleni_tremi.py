cislo = int(input("Zadej číslo s koncovou číslicí 8: "))

if cislo % 10 == 8: #Toto zjistí jestli se poslední číslice zadanéhé čísla rovná číslu za ==. tento řádek říká že když
                    # po vydělení 10 je ZBYTEK 8 tak pokračuj
    vypocet = cislo % 3 # % je ZBYTKOVÉ DĚLENÍ
    if vypocet == 0:
        print("Číslo je dělitelné 3.")
    else:
        print("Číslo má na konci 8, ale není dělitelné 3.")
else:
    print("Číslo nemá na konci 8.")