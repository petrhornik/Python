"""Kromě metody .append, která přidává jediný prvek, existuje metoda .extend, která umí přidávat prvků víc.
    Prvky k přidání jí předáme ve formě seznamu             """

prvocisla = [2, 3, 5, 7, 11, 13, 17]
dalsi_prvocisla = [23, 29, 31]
prvocisla.extend(dalsi_prvocisla)
print(prvocisla)
print()

"""Metoda .extenbd umí pracovat i s jinými typy než seznamy - ráda zpracuje cokoli, přes co umí cyklit for:
    např. jednotlivé znaky řetězců, řádky souborů, nebo čísla z range().                                    """
seznam = []
seznam.extend("abcdef")
seznam.extend(range(10))
print(seznam)