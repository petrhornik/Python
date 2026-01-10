from random import randint
hod = randint(1, 6)

def hod_kostkou():
    return hod

x = int(input("Kolikčrát si přeješ házet? "))

for i in range(x):
    print(hod_kostkou())