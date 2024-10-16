try:
    neco_udelej()
except ValueError:
    print("Tohle se provede, pokud nastane ValueError")
except NameError:
    print("Tohle se provede, pokud nastane NameError")
except Exception:
    print("Tohle se provede, pokud nastane jiná chyba")

except TypeError:
    print("Tohle se neprovede nikdy")

else:
    print("Tohle se provede, pokud chyba nenastane")
finally:
    print("Tohle se provede vždycky; i pokud v try bloku byl např. return")
print()