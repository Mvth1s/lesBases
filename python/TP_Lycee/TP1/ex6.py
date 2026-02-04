
from random import randrange

# Besoin 1
print("----------Besoin n°1----------")

print("Quel est la longueur du rectangle ?")
longueur = int(input())
print("Quele est la largeur du rectangle ?")
largeur = int(input())

aire = longueur * largeur
perimetre = 2 * (longueur + largeur)
print("L'aire du rectangle est de : ", aire)
print("Le périmètre du rectangle est de : ", perimetre)

# Besoin 2
print("----------Besoin n°2----------")

print("Quel âge as-tu ?")
age = int(input())
if age >= 12:
    print("Tu es un 'Cadet' !")
elif age >= 10 & age <= 11:
    print("Tu es un 'Minime' !")
elif age >= 8 & age <= 9:
    print("Tu es un 'Pupille' !")
elif age >= 6 & age <= 7:
    print("Tu es un 'Poussin' !")

# Besoin 3
print("----------Besoin n°3----------")

print("Combien de photocopie voulez-vous faire ?")
nbr_photocopie = int(input())

if nbr_photocopie <= 10:
    facture = nbr_photocopie * 0.10
elif nbr_photocopie <= 30:
    facture = 10 * 0.10 + (nbr_photocopie - 10) * 0.09
else:
    facture = 10 * 0.10 + 20 * 0.09 + (nbr_photocopie - 30) * 0.08

print("Cela vous coûtera :", facture, "EUR")

# Besoin 4
print("----------Besoin n°4----------")

print("Quel est le nombre de carré sur un coté ?")
nbr_carre = int(input())
somme = 0
for i in range(1, nbr_carre + 1):
    somme = somme + i**2
print("le nombre de carrée pour ", nbr_carre,"est de : ", somme)

# Besoin 5
print("----------Besoin n°5----------")

# from random import randrange # importer au début du fichier
nbr_cout = 8
nbr_a_trouver = randrange(0,100)
num_essai = 1
print("Taper un nombre entre 0 et 100 !")
while num_essai <=nbr_cout:
    nbr = int(input())
    
    if nbr < nbr_a_trouver:
        print("Plus grand !")
    elif nbr > nbr_a_trouver:
        print("Plus petit !")
    else:
        print("Vous aves trouvez le bon numéran en ", num_essai, "essai(s) sur ", nbr_cout)
        break
    
    num_essai = num_essai + 1