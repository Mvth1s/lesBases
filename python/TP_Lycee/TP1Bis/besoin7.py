
# Besoin 7
print("----------Besoin n°7----------")

nbr_liste = []

print("Veuiller choisir 20 nombres :")

for i in range(1, 21):
    nbr = int(input("Entrer le nombre numéro " + str(i) + " : "))
    nbr_liste.append(nbr)
    
nbr_plus_grand = 0
for j in nbr_liste:
    if j > nbr_plus_grand:
        nbr_plus_grand = j
        
print("Le nombre le plus grand de la liste fournit est : ", nbr_plus_grand)