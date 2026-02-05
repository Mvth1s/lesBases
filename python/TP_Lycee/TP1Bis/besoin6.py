
# Besoin 6
print("----------Besoin n°1----------")

print("Veillez choisir une nombre de départ !")
nbr_depart = int(input())

factoriel = 1
for i in range(1, nbr_depart+1):
    factoriel = factoriel * i

print("La factoriel de ", nbr_depart, " est : ", factoriel)