from random import randint

body = 0

while True:
    print(body)
    odpoved = input("Otočit kartu? ")

    if odpoved == "ano":
        cislo = randint(1, 11)
        print("Cislo:", cislo)
        body = body + cislo
        if body < 21:
            continue
        elif body == 21:
            print("Výhra!\nVáš počet bodů je roven 21!")
            break
        else:
            print("Prohra!!!")
            print("Počet bodů je:", body)
            print("Váš počet bodů přesáhl 21 o:", body - 21)
            break
    else:
        print("Konec!")
        break

