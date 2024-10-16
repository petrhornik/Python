x = 0

def nastav_x(hodnota):
    # global x
    x = hodnota     # přiřazení do lokální proměnné

nastav_x(40)
print(x)

# tyto proměnné jsou lokální proměnné
        # existují jen v místě, v rámci volání jedné jediné funkce

# proměnné, které nejsou lokální, jsou globální
        # existují v celém programu (Jen ve funkcích, které mají náhodou lokální proměnnou stejného jména, "nejsou vidět")