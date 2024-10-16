from random import randint

def pin():
  for i in range(4):
      print(randint(0,9), end=" ")

print("PIN:", end=" ")
pin()