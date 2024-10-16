x = input("Zadej text:")

for znak in x:
    if znak in "aeiouAEIOU":
        print(znak, end= " ")

# řešení 2

x = input("Zadej text:")
sam = "aeiouAEIOU"

for znak in text:
    if znak in sam:
        print(znak, end= " ")