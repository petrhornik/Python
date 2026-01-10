# Zanoření podmínek - jedná se o podmínku v podmínce takže pokud je např: šťastný ale ne bohatý, program
# vypíše "Zkus míň utrácet".

stastny = input("Jsi šťastný? ")
bohaty = input("Jsi bohatý? \n")

if stastny == "ano": #Tenhle kus kódu se provede, když je šťastný. [V podmínce if a elif nemusí být závorky :)]
    if bohaty == "ano":
        print("Gratuluji!")
    else:
        print("Zkus míň utrácet!")

else: #Tenhle kus kódu se provede když není šťastný.
    if bohaty == "ano":
        print("Zkus se víc usmívat")
    else:
        print("To je mi líto.")