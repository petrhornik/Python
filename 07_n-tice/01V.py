

def vnejsi_funkce():
    return vnejsi_funkce(0)

def vnitrni_funkce(delitel):
    return 1 / delitel

print(vnejsi_funkce())

"""Na začátku si ukážeme, jak python vypíše chybu, která nastane v zanořené funkci:"""

"""
Traceback (most recent call last):
  File "/Users/lachtanek/PycharmProjects/PythonT3A/07Vyjimky/01V.py", line 7, in <module>
    print(vnejsi_funkce())
          ^^^^^^^^^^^^^^^
  File "/Users/lachtanek/PycharmProjects/PythonT3A/07Vyjimky/01V.py", line 2, in vnejsi_funkce
    return vnejsi_funkce(0)
           ^^^^^^^^^^^^^^^^
TypeError: vnejsi_funkce() takes 0 positional arguments but 1 was given
"""
