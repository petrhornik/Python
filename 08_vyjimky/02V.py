cislo = int(input("Zadej číslo k oveření: "))
velikost_pole = 20

def over_cislo(cislo):
    if 0 <= cislo < velikost_pole:
        print("OK")
    else:
        raise ValueError("Číslo {n} není v poli!" .format(n=cislo))
over_cislo(cislo)


"""Výpis chyby:"""

"""
Traceback (most recent call last):
  File "/Users/lachtanek/PycharmProjects/PythonT3A/07Vyjimky/02V.py", line 9, in <module>
    over_cislo(cislo)
  File "/Users/lachtanek/PycharmProjects/PythonT3A/07Vyjimky/02V.py", line 8, in over_cislo
    raise ValueError("Číslo {n} není v poli!" .format(n=cislo))
ValueError: Číslo 21 není v poli!
"""

