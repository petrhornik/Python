# funkce je potřeba volat
# když nenapíšu závorky, funkce se nezavolá! (nedostanu návratnou hodnotu, ale samotnou funkci.)
# např:

from math import sin

print(sin(1)) # spočítá sinus 1 a vypíše to
print(sin)    # chybné volání sinu bez závorek
              # závorky jsou k printu
print(sin + 1)

import math
promenna = math.sin(1)
print(promenna) # spočítá sinus 1 a vypíše to