adamM = int(input("Zadej známku Adama z M: "))
adamCJ = int(input("Zadej známku Adama z ČJ: "))
tomasM = int(input("Zadej známku Tomáše Z M: "))
tomasCJ = int(input("Zadej známku Tomáše z ČJ: "))
krystinaM = int(input("Zadej známku Krystýny z M: "))
krystinaCJ = int(input("Zadej známku Krystýny z ČJ: "))

a = (adamM + adamCJ) / 2
t = (tomasM + tomasCJ) / 2
k = (krystinaM + krystinaCJ) /2

if(adamM >= 1 and adamM < 6 and adamCJ >= 1 and adamCJ < 6 and tomasM >= 1 and tomasM < 6 and tomasCJ >= 1 and tomasCJ < 6 and krystinaM >= 1 and krystinaM < 6 and krystinaCJ >= 1 and krystinaCJ < 6):
    print(a)
    if(a >= 4.2):
        print("Adam neprošel!")
    else:
        print("Adam prošel!")
    print(t)
    if(t >= 4.2):
        print("Tomáš neprošel!")
    else:
        print("Tomáš prošel!")
    print(k)
    if(k >= 4.2):
        print("Krystýna neprošla!")
    else:
        print("Krystýna prošla!")
else:
    print("Neplatný vstup!!!")