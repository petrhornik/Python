# retezec === string

mystring = "cokolada" # array je iterable

fifth_num = mystring[5] # znaky ve stringu se dají jednotlivě manipulovat
stejne_odkonce = mystring[-3] # platí i od konce
print(fifth_num)
print(stejne_odkonce)

print("\n")

for i in range(len(mystring)): # lze iterovat přes něj
    print(mystring[i])

print("\n")

# len() fce je pro měření délky ()hl. u iterable
newstring = "Dobrý den, jmenuji se John Doe"
lengthofstr = len(newstring)
print("Delka stringu", lengthofstr)

# array (list)

list1 = ["skoda", "fiat", "volvo"]
print("Delka listu", len(list1))

# tuple (n-tice) - list položek neměnitelný (vždy zůstane tak jak je prve definován)

myTuple = ("leden", "unor", "brezen", "duben")
print("Delka tuple",len(myTuple))

print("\n")

# metody (pro string, list, ...)
retezec = "Tomas Kumulala"
print(retezec.upper())
print(retezec.lower())
print(retezec)

# něco jako fce., dá se zavolat.
# vždy je svázaná k nějakému objektu (string, list, ...)
# přidáme je za objekt pomocí . notation

print("\n")

# výběr kusu retezce -> [start:stop:step]

piece = mystring[5:]
print(piece)

print(mystring[2:5])
print(mystring[-4:])
print(mystring[::2])

# stop hodnota se nikdy nevypíše
