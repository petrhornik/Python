# Při tisku např. tabulek nějakých hodnot často potřebujeme slušně naformátovat takový vstup např.:

for i in range(1,11):
    print(i, i * i, i ** 3, i ** 4)

print()

# Nejčastěji použijeme formátování znakového řetězce (metodou format ()):


for i in range(1,11):
    print("{:3} {:4} {:5} {:6}".format(i, i * i, i ** 3, i ** 4))

# {} = altgr + B, N