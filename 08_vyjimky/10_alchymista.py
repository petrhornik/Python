"""mudrc psal své spisy šifrovaně
použij všdy první a čtvrté písmeno"""

zasifrovany_text = ["Praha", " t2ts", "éfgto", "oki Kl", "ldráf", "t45knn", "yHr !", "jdrewer", " hj6kl", ",gk8Rtyně", ".zv tlo se", "Pjhott", "zwfohh", "rík!"]

text = ""
pocet = 0

for slovo in zasifrovany_text:
    text = text + slovo[0] + slovo[3]
    pocet = pocet + 1

print("Počet slov je:", pocet)
print(text.upper())

print("Petr Horník - T3A")


