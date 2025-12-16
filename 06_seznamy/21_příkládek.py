import random

dívky = ["Marcela", "Anička", "Petra", "Terezka", "Miška"]
chlapci = ["Lukáš", "Jeník", "Petr", "Kubík", "David"]

for i in range(len(chlapci)):
    random.shuffle(dívky)
    random.shuffle(chlapci)
a = chlapci.pop()
b = random.choice(dívky)

print(chlapci, "-", dívky)