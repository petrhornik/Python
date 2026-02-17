# seznam === list === array
# může obsahovat více hodnot

nums = [1,1,6,3,5,8,13]
print(nums[2])

# lze si určit více hodnot pomocí :

print(nums[2:-2])

# lze připojit array za array pomocí .extend() <- či přidat více hodnot najednou

moreNums = [20,21,22,23,24]
nums.extend(moreNums)
print(nums)

#umí pracovat i s jinnými typy než se seznamy (array) -> zpracuje jakoukoli iterable jako cykl for

seznam = []
seznam.extend("Ahoj Tome") # iteravle string se uloží po jednotlivých znacích
seznam.extend(range(10)) # přidá každé číslo z range
print(seznam)

# .extend x .append
# .append -> přidá celou hodnotu najednou ("Ahoj" -> přidá jako ["Ahoj"])
# .extend -> přidá jednotlivé znaky -> iteruje ("Ahoj" -> přidá jako ["A", "h", "o", "j"])

# v seznamech lze měnit jednotlivé prvky pomocí bracket notation

newNums = [1, 0, 5, 32]
newNums[2] = 61
print(newNums)

# lze přidat na tuto pozici i celé nové pole (podseznam)
# nahradí se původní hodnoty a je jedno kolik nových přijde

newNums[1:-1] = [11, 11, 11] # jako .extend umí zpracovat jakoukolui iterable (arr, string, rage(), ...)
print(newNums)