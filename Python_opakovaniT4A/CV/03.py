import random
from random import shuffle

# Moje řešení
girls = ["Maruška", "Anička", "Petra", "Terezka", "Miška"]
boys = ["Tom", "Jeník", "Petr", "Kubík", "David"]
mixed = []

for i in range(len(boys)):
    chlapec = boys[random.randint(0, len(boys)-1)]
    boys.remove(chlapec)
    divka = girls[random.randint(0, len(girls) - 1)]
    girls.remove(divka)
    mixed.append(chlapec + " + " + divka)

for i in range(len(mixed)):
    print(mixed[i])


# Tabule
random.shuffle(girls) # shuffle() -> fce. pro náhodné zamíchání prvků v iterable
random.shuffle(boys)

for boy, girl in zip(boys, girls):
    print(boy + " " + girl)