def nacti_cislo():
    while True:
        try:
            odpoved = int(input("Zadej číslo: "))
            print("správně jsi zadal číslo.")
            return odpoved
        except ValueError:
            print("to nebylo číslo! Zkus to znovu.")

nacti_cislo()