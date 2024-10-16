slova = "Tato věta je složitá, rozdělujeme ji na slova!".split()
print(slova)
print()

"""Metoda split umí brát i argument. Pokud ho předáme, místo mezer (a nových řádků) se řetězec "rozseká daným
    oddělovačem. Takže když máme nějaká data oddělená čárkami, není nic jednodušího než použít split s čárkou:"""

zaznamy = "3A,8N,2E,9D".split(",")
print(zaznamy)
print()

"""Chceme-li spojit seznam řetězců zase dohromady do jediného řetězce, použijeme metodu join
    Pozor, tahle metoda se volá na oddělovači, tedy řetězci, kterým se jednotlivé kousky "slepí" dohromady; a jako
    argument bere seeznam jednotlivých řetězců"""

veta = " ".join(slova + zaznamy)
print(veta)