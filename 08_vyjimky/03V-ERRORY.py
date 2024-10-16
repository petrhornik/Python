"""
TYPY ERRORU

BaseException
    SystemExit          vyvolána funkcí exit()
    KeyboardInterrupt   vyvolána po stisknutí Ctrl+C
    Exception

ArithmeticError
    ZeroDivisionError dělení nulou
AssertionError      nepovedený příkaz assert
AttributeError      Neextistující atribut, např. "abc".len
ImportError         nepovedený import
LookupError
    IndexError      Neexistující index, např. "abc"[999]
NameError           použití neexistujícího jména proměnné
    UnboundLocalError   použítí proměnné, která ještě nebyla nastavená
SyntaxError         špatná syntaxe - program je nečitelný/nepoužitelný
    IndentationError Špatné odsazení
        TabError    Komninování mezer a tabulátoru
TypeError           špatný typ, např. len(9)
ValueError          špatná hodnota, např. int("xyz")

"""