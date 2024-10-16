sifra = ["Maaea", "amaudet", "iá,iPfrfd", "Maaadkzuhud", "ivi i", "sPtyuP", "tteh", "eoďnk","jj!!5"]
text = ""
poradi1 = -1
poradi2 = 0
cast1= ""
cast2 = ""


for slova in sifra:
    if poradi1 < -3:
        poradi1 = -1

    if poradi2 > 5:
        poradi2 = 0


    cast1 = cast1 + slova[poradi1]
    poradi1 = poradi1 - 1
    cast2 = cast2 + slova[poradi2]
    poradi2 = poradi2 + 1

x = list(zip(cast2, cast1))
y = "".join([f"{cast2}{cast1}" for cast2, cast1 in x])
print(y)