celkem = 200
prodano = 50
cena = 150


print('Cena vstupenky: 150 Kč')
pocet = int(input('Kolik chceš vstupenek: '))

if pocet <= 150:
    print('Vstupenky ještě máme, za svoje vstupenky zaplatíš', pocet * 150, 'Kč')
    print('Ještě zbývá', celkem - pocet , '(',((celkem - pocet) / celkem *100 ),'% )', 'vstupenek')
else:
    print('Tolik vstupenek už nemáme!')
