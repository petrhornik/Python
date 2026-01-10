plocha = int(input(" Zadej zastavěnou plochu stavby: "))
vzdalenost = int(input("Zadej vzdálenost stavby od sousedního pozemku: "))

if(vzdalenost > 2):                                                  # když je vzdalenost větší než 2 tak pokračuj
    if(plocha > 30):                                                 # když bude plocha větší než 30 pokračuj
        print("Stavební povolení je potřeba!")                       # toto se vypíše kdyže je to nad tím pravda
    else:                                                            # když není if(plocha > 30) pravda, provede se else
        print("Stavební povolení není potřeba!")
else:
    print("Stavební povolení je třeba!")
