pohlavi = input("Zadej pohlaví: ")
pivo = int(input("Před kolika minutami bylo vypito 1 pivo: "))
zena = (240 - pivo)
muz = (180 - pivo)


if pohlavi == 'muž':
    if muz <= 0:
        print('Můžeš řídit!')
    else:
        print('Můžeš řídit za', muz ,'minut')


elif pohlavi == 'žena':
    if zena <= 0:
        print('Můžeš řídit!')
    else:
        print('Můžeš řídit za', zena ,'minut')

