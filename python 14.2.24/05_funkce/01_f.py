# Psaní vlastních funkcí.

# = definuje se příkazem def, za nějž napíšeme jméno funkce, pak do závorky seznam argumentů(které funkce bere),
#   a dvojtečku.

# - poté následuje odsazené tělo funkce s příkazy, které funkce provádí.
# - Tělo funkce může začít dokumentačním řetězcem, který popisuje, co funkce dělá.


def obvod_obdelnika(sirka, vyska):
    "Vrátí obvod obdélníka daných rozměrů."
    return 2 * (sirka + vyska)                      # - příkazem return můžeme z funkce vrátit nějakou hodnotu.

print("Obvod obdélníka je:",obvod_obdelnika(4, 2))