#funkce, která vrátí obsah elipsy daných rozměrů.
#příslušný vzorec je A = pi*a*b, kde a a b jsou délky os.

from math import pi

def obsah_elipsy(a, b):
    return pi * a * b

print("Obsah elipsy s osami 3cm a 5cm je:", obsah_elipsy(3, 5), "cm2")

# řešení #2

from math import pi

def obsah_el(a, b):
   print("Obsah je:", pi * a * b) # pozor {print} místo {return}

obsah_el(3, 5)

# popis řešení #2
    #program takhle funguje, ale přichází o jednu z hlavních výhod funkcí: mežnost vrácenou hodnotu použít i v...