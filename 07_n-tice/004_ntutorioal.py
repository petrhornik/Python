""" Python umí jěště jeden trik:
    pokud chci přiřadit do několika proměnných najednout, stačí je na levé straně rovníku oddělit čárkou
    a na pravou stranu dát nějakou 'složenou' hodnotu - třeba právě n-tici. """

def podil_a_zbytek(a, b):
    return a // b, a % b
podil, zbytek = podil_a_zbytek(12, 5)
print(podil,zbytek)

""" N-tice se k tomuto účelu hodí nejvíc, ale jde to se všemi hodnotami, které jdou použít ve for:"""