def ano_nebo_ne(otazka):
    "Vrátí True nebo False, podle odpovědi uživatele"
    while True:
        odpoved = input(otazka)
        if odpoved == "ano":
            return True
        elif odpoved == "ne":
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')

if ano_nebo_ne("CHceš si zahrát hru? "):
    print("OK! Ale napřed ji musíš naprogramovat.")
else:
    print("Škoda.")