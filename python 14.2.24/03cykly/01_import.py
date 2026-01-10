# Dříve jsme do programuz zadali hodnotu [pi] natvrdo.
# Python má ale spoustu vychytávek zabudovaných - není třeba je psát, ale musíme vědět, kam se podívat.
# Pi si zpřístupníme importem modulu math.

#1 přímo z knihovny math naimportuj pouze číslo pi a vypiš
from math import pi
print(pi)

#2 nebo takto:
import math         #naimportuj celou knihovnu math
print(math.pi)      #naimportuj z knihovny math číslo pi a vypiš