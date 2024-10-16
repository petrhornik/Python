"""Leonarde psal do svých starých spisů šifrované poznámky. Naprogramuj dešifrovací stroj.
    Při šifrování se skrývá zpráva do běžných i podivných slov. Při dešifrování se použije z paždého slova 1. a 2. pismeno."""

zasifrovany_text = ["aNakonda", "uzdeří", "pár", "rek", "v, čem", "ato hned", "ahlava", "ke mně", "rbyse", "nl mně", "zvrtlo se", "otunit", "plnička", "gík!", "n. jkkllert"]

#moje řešení
"""
prvni_pismeno = [item[1] for item in zasifrovany_text]  
druhe_pismeno =[item[2] for item in zasifrovany_text]

spojeni_pismen = list(zip(prvni_pismeno, druhe_pismeno))

spojeni_pismen_string = ''.join([f"{prvni_pismeno}{druhe_pismeno}" for prvni_pismeno, druhe_pismeno in spojeni_pismen])

print(spojeni_pismen_string)
"""

# z tabule
sifra = ""

for slovo in zasifrovany_text:
    sifra = sifra + slovo[1] + slovo[2]        # do šifry se načítají jednotlivá písmena(v tomto případě 1. a 2.)
                                                # tohoto jsme dosáhli pomocí indexu
print(sifra)
