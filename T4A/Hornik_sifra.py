# Jsem programátor!
# klíč: 1. pismeno šifry bude 1. pismeno z 1. slova
#       2. pismeno bude posledni pismeno z posledniho slova.

zasifrovany_text = ["Jgterge", "Egrge", " Peste", "Rests", "Gtgertgs", "Aerger","Aerger","Otgeh","!egegerg","gege!","ghtrhrtR","ghtrhT","gergeM","hhtrhrR", "htrhrthtO", "rgherghP", "gherherhM", "ghegheS"]
text = ""
text2 = ""

"""polovina = len(zasifrovany_text) // 2

prvni_pulka = zasifrovany_text[:polovina]
druha_pulka = zasifrovany_text[polovina:]

print(prvni_pulka)
print(druha_pulka[::-1])

for slovo in prvni_pulka:
    text = text + slovo[0]
for slovo in druha_pulka:
    text2 = text2 + slovo[-1]

print(text)
print(text2)

text_uprava = text2

spojeni_pismen = list(zip(text, text2[::-1]))
spojeni_pismen_text = "".join([f"{text}{text2}" for text, text2 in spojeni_pismen])

print(spojeni_pismen_text)
"""


poradi = 0
pocet = 0

for slovo in zasifrovany_text:
    poradi = poradi + 1

pocet_kroku = poradi / 2

print(pocet_kroku)

for slovo in zasifrovany_text:
    if pocet < pocet_kroku:
        text = text + slovo[0]
        pocet = pocet + 1
    else:
        text2 = text2 + slovo[-1]


print(text)
print(text2)

spojeni_pismen = list(zip(text, text2[::-1]))
spojeni_pismen_text = ''.join([f"{text}{text2}" for text, text2 in spojeni_pismen])

print(spojeni_pismen_text)
