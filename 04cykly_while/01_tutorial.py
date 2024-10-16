# while - 2. typ cyklu (z angl. přeloženo jako DOKUD)
# Na rozdíl od for, kde předem je známe počet opakování, se while používá, když cyklus závisí na nějaké podmínce.
# Tělo cyklu se opakuje, dokud je podmínka splněna.

# např:
odpoved = input("Řekni Ááá! ")

while odpoved != "Ááá!":
    print("Špatně, zkus to znovu")
    odpoved = input("Řekni Ááá! ")