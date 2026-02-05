
# Besoin 8
print("----------Besoin n°8----------")

print("Veiller prendre un nombre en binaire !")
nbr_binaire = input()

# Méthode 1
nbr_decimal = int(nbr_binaire, 2)
print("Le nombre binaire '" + str(nbr_binaire) + "' correspond a :", nbr_decimal)

# Méthode 2
nbr_dec = 0
puissance = len(nbr_binaire) - 1

for chiffre in nbr_binaire:
    if chiffre == 1:
        nbr_dec += 2 ** puissance
    puissance -= 1

print("Le nombre binaire '" + str(nbr_binaire) + "' correspond a :", nbr_decimal)
