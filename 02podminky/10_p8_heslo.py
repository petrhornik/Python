heslo = str(input("Zadej číselné heslo:")) #pokud chci použít string str(input(""))) do tohoto příkazu se dají psát
                                           #čísla i písmena, ALE VŠECHNY ZNAKY JSOU BRÁNY JAKO TEXT
if(heslo == "55869"):               #01 když používám string tak musim dát heslo(ty znaky) do ""
    print("Správné heslo!")
else:
    print("Špatné heslo!")