def nacti_cislo():
    odpoved = input("Zadej číslo:")
    try:
        cislo = int(odpoved)
    except ValueError:
        print("To nebylo číslo! Pokračuj s nulou.")
        cislo = 0
    return cislo
nacti_cislo()
