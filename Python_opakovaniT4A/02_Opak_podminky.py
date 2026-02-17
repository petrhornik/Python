# python -> if, elif, else

## doplnit kontrolu platného dne v měsíci

num =  ""

while len(num) < 11 or len(num) > 11:
    num = input("Zadej 10 místné rodné číslo: ")
    if len(num) < 11 or len(num) > 11:
        print("Zadali jste neplatné číslo!!")

rodCis = num[7:]
dayNum = num[4:6]

if int(rodCis) % 11 == 0:
    print("platné")
    mesic = str(num[2:4])
    print(mesic)
    if (0 < int(mesic) <= 12) or (50 < int(mesic) <= 62):
        if int(mesic) > 50:
            print("Číslo patří ženě!")
            newMesic = int(mesic) - 50
            if newMesic < 10:
                newMesic = "0" + str(newMesic)
                newDate = num.replace(str(mesic), str(newMesic))
            else:
                newDate = num.replace(str(mesic), str(newMesic))
        else:
            print("Číslo patří muži!")
            newDate = num
    else:
        print("Měsíc není platný")

    print(newDate, "<- přepsané datum")
else:
    print("číslo nelze dělit 11!!")






