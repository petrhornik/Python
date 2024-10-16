"""Seznam se dá použít v příkazu if (nebo while) jako podmínkam která platí, když v tom seznamu něco je.
    Jinými slovy, seznam je tu "zkratka" pro len(seznam) > 0."""

seznam = [1, 2]
if seznam:
    print("V seznamu něco je!", seznam)
else:
    print("Seznam je prázdný...")