from knihovna_elipsa import obsah_elipsy #import mnou vytvořené knihovny, konkrétně fce {obsah_elipsy}

def objem_eliptickeho_valce(a, b, vyska):
    return obsah_elipsy(a, b) * vyska

print("Objem eliptickeho válce je:", objem_eliptickeho_valce(3, 5, 3))