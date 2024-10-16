from random import randrange

while True: # dokud je pravda, číslo je do 10000
    print("Číslo je", randrange(10000))
    print("Počkej než se počítač unaví!")

# Pozor! Je velice jednoduché napsat cyklus, jehož podmínka bude splněna vždycky.
# Takový cyklus se bude opakovat donekonečna. Program se dá přerušit pomocí [Ctrl + C].