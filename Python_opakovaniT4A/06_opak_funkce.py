def insert_money(account, user):
    while True:
        print(f"Aktuální zůstatek na účtu {user}:", account, "Kč")
        try:
            insert = int(input("Vložit peníze (0 a menší -> ukončení): "))
            if insert <= 0:
                break
            account += insert
            print("Váš zůstatek je:", account, "Kč")
            return account
        except (ValueError, TypeError):
            print("Zadali jste neplatnou hodnotu")

def withdraw_money(account, user):
    while True:
        print(f"Status účtu uživatele {user}:", account, "Kč")
        try:
            withdraw = int(input("Částka k výběru (0 a menší -> ukončení): "))
            if withdraw <= 0:
                break
            account -= withdraw
            if account < 0:
                print("Nedostatečný limit!!")
                account += withdraw
                continue
            print("Váš zůstatek je:", account, "Kč")
            return account
        except (TypeError, ValueError):
            print("Zadali jste neplatnou hodnotu")

def check_balance(account, user):
    print("Účet uživatele", user, "ubsahuje sumu:", account, "Kč")


while True:
    try:
        name = str(input("Zadejte přihlašovací jméno: "))
        zustatek = int(input("Zadejte zůstatek na účtu "))
        break
    except (ValueError, TypeError):
        print("Zadali jste neplatnou hodnotu")

while True:
    try:
        print("-- BANK SYSTEM --")
        print("1 - Vložit peníze")
        print("2 - Vybrat peníze")
        print("3 - Zkontrolovat zůstatek")
        print("4 - Odejít ze systému\n")
        option = int(input("Vyberte položku: "))
        if option == 1:
            zustatek = insert_money(zustatek, name)
        elif option == 2:
            zustatek = withdraw_money(zustatek, name)
        elif option == 3:
            check_balance(zustatek, name)
        elif option == 4:
            print("Děkujeme, že využíváte naše služby!\n")
            break

    except (ValueError, TypeError):
        print("Zadali jste neplatnou hodnotu!!\n")