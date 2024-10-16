zasifrovany_text = ["Have", "kalumet", "pár", "Marie", "vida,", "ertzuz", "pátek", "eěrrk","jjt45", "kok osvv", "wswkna", "ahojda", "jábajka", "azerbaj", "kdáksde", "mvnkkko", "sdfgle", "hjklpa", "dioptrický", "anenský", "studie", "hah!ddd"]

poradi = 0  # na začátku se vynuluje pořadí
sifra = ""  # na začátku se nadefinují proměnné

for slovo in zasifrovany_text:  # pro každé slovo ze seznamu zasifrovany_text se projde cyklem for
    if poradi > 5:  # když je slovo v pořadí více než 5
                    # tak se vynuluje pořadí, určuje kolikáté písmeno ze slova bere do dešifrovaného textu
        poradi = 0
    sifra = sifra + slovo[poradi]   # do šifry se načítají jednotlivá písmenka z těch slov ze
    poradi = poradi + 1     # na konci je počítadlo, při každém průchodu cyklem for se poradi zvýšý o 1

print("Zpráva zní:", sifra)