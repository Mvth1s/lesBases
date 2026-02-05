
# Besoin 9
print("----------Besoin n°9----------")

print("Veiller prendre un nombre en binaire !")
nbr_binaire = input()

# Méthode 1
nbr_hexadecimal = hex(int(nbr_binaire, 2))
print("Le nombre binaire '" + str(nbr_binaire) + "' correspond a :", nbr_hexadecimal)

