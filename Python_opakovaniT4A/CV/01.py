# moje
myname = str(input("Zadejte své jméno: "))
initials = ""
wordArr = myname.split(" ")
for word in wordArr:
    initials += word[0].upper() + " "
print(initials)

#tabule
jmeno = input("Zadej jmeno: ")
prijmeni = input("Zadej prijmeni: ")
inicialy = jmeno[0] + prijmeni[0]
print(inicialy.upper())