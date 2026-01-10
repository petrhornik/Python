x = int(input())

def plus_minus():
    print("+--" * x, end="+\n")

def lomitko():
    print("|  " * x, end="|\n")             # | se píše pomocí {AltGR  + W}

for i in range(2):
    plus_minus()
    lomitko()
plus_minus()
