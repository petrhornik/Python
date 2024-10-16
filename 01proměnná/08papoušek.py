# Reakce na vstup uživatele. Napíšeme program papoušek, který bude dvakrát opakovat to, co uživatel napsal.

# 1. řešení
Slovo = input("Napiš něco: ")
print(Slovo, Slovo)

# 2. řešení
Slovo = input("Napiš něco: ")
print((Slovo + " ") * 2)

# 3. řešení
Slovo = input("Napiš něco: ")
print(Slovo + " " + Slovo)

# 4. řešení

Slovo = input("Napiš něco: ") # získá od uživatele vstup a uloží jej do proměnné
výsledek = slovo + " " + slovo # vytvoří novou proměnnou
print(výsledek)