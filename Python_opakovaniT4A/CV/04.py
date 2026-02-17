myStr = input("Zadej nějaký text: ")
print(len(myStr))
for i in range(3): print(f"{i + 1}. znak: ",myStr[i])
print("Poslední znak:", myStr[-1] )
for i in range(len(myStr)): print(myStr[i], end=" ")

# String v proměnné, vypiš délku, určité znaky a přes cykl for