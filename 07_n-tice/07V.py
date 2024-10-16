
def strana_ctverce():
    while True:
        try:
            strana = int(input('Zadej stranu čtverce v centimetrech: \n'))
            print("zadal jsi správně rozměr.\n")
            print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
            print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
            return strana
        except ValueError:
            print("Špatně zadaná hodnota rozměru. Zkus to znova.\n")

strana_ctverce()
