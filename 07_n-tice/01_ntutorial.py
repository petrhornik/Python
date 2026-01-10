""" Chovají skoro stejně jako seznamy, jen nejdou měnit.
    Nemají metody jako append a pop a nedá se jim přiřazovat do prvků
    Dají se ale použít v cyklu for a dají se z nich číst jednotlivé prvky."""

osoby = "máma", "teta", "babička"
for osoba in osoby:
    print(osoba)

""" print('První je {}'.format(osoby[0])) """
print("První je",osoby[0])

""" N-tice jsme použili už dříve:
        for jmeno in 'Hynek', 'Vilém', 'Jarmila':
    ve skutečnosti používá n-tici!!! """