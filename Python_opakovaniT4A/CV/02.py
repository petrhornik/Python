# moje reseni
sentence = "Eva má malou marmeládovou svačinu"
newSentence = sentence.replace("a", str(ord("a"))) # replace pro změnu všech stejných znaků za jinné
newString = ""
print(newSentence)

#moje reseni no.2

for char in sentence:
    if char == "a":
        newString += char.replace("a", str(ord("a")))
    else:
        newString += char

print("\n" + newString)

# tabule
for char in sentence:
    if char == "a":
        print(ord(char), end = "")
    else:
        print(char, end = "")
