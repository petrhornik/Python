"""Mame radi python"""

zasifrovany_text = ["aMoao", "nmael", "l,r eam", "ereaeee", "gdrihrt", "a rpi", "fygta", "hhtohrt", "ong.dgde" ]

text = ""
pocet = 0

for slovo in zasifrovany_text:              #pro počet slov v zašifrovaném textu
    text = text + slovo[1] + slovo[3]       # Přičteme 1 a 3 písmeno k textu z kazdeho slova
    pocet = pocet + 1                       # počítadlo počtu slov

print("Počet slov je:", pocet)      #počet slov
print(text)                         #šifra


sifra = ["Maaee", "raaudet", "iámiP", "Maree", ",vid,", "rrtrur", "áátea", "eďďrk","jjii5", "k,kh hftr", "PswkPa", "ayztjtzju", "tátajka", "ahehbaj", "kdokode", "nvnnkko", "d.fjgte"]

slova = ""      #proměnná pro větu
poradi = 0      #poradi pismena

for i in sifra:        #pro počet slov ve šifře
    if poradi > 4:      #pokud je poradi vetsi než 4
        poradi = 0      #vynuluje se
    slova = slova + i[poradi]  # přičteme ke větě pismeno dle poradi z každého slova
    poradi = poradi + 1        #pocitadlio poradi(při kazdem cyklu se pricte 1)

print(slova)        #vypise slova