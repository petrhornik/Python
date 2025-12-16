x = int(input("Zadej vysku pyramidy: "))
znak = input("Zadej znak: ")

def pyramida():
    for a in range(2):
        for i in range(x):
            v = (znak + " ") * i
            center = v.center(x * 3)
            print(center)

pyramida()
