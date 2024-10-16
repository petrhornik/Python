import random
mozne_tahy = ["kámen", "nůžky", "papír"]
tah_pc = random.choice(mozne_tahy)
tah_cloveka = input ("Zadej kámen, nůžky nebo papír: ")
print("Počítač vybral:", tah_pc)
# [] - označují seznam

if(tah_cloveka == "kámen"):
    if(tah_pc == "kámen"):
        print("Nikdo nevyhrál!")
    elif(tah_pc == "nůžky"):
        print("Výhrál jsi!")
    else:
        print("Prohra!")
elif(tah_cloveka == "nůžky"):
    if(tah_pc == "kámen"):
        print("Prohra!")
    elif(tah_pc == "nůžky"):
        print("Nikdo nevyhrál!")
    else:
        print("Výhra!")
elif(tah_cloveka == "papír"):
    if(tah_pc == "kámen"):
        print("Výhra!")
    elif(tah_pc == "nůžky"):
        print("Prohra!")
    else:
        print("Nikdo nevyhrál!")
else:
    print("Neplatný vstup!!!")