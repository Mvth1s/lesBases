## ----------La calculatrice---------- ##

# -*- coding: utf-8 -*- #
from math import *
from tkinter import *

# initialisation des variables
valeur, operation, point, puissance = 0, 0, 0, 1


# création des fonctions nécessaires
def nombre(touche):
    global valeur, point, puissance
    if point == 0:
        valeur = valeur * 10 + touche
    else:
        valeur = valeur + touche / (10 ** (puissance))
        puissance = puissance + 1
    affichage.set(str(valeur))


# fonctions liées aux boutons
def x0():
    nombre(0.0)


def x1():
    nombre(1.0)


def x2():
    nombre(2.0)


def x3():
    nombre(3.0)


def x4():
    nombre(4.0)


def x5():
    nombre(5.0)


def x6():
    nombre(6.0)


def x7():
    nombre(7.0)


def x8():
    nombre(8.0)


def x9():
    nombre(9.0)


def virgule():
    global point
    point = "."


def aplus():
    global operation, sauvegarde, valeur, point, puissance
    operation = "+"
    valeur, sauvegarde, point, puissance = 0, valeur, 0, 1


def amoins():
    global operation, sauvegarde, valeur, point, puissance
    operation = "-"
    valeur, sauvegarde, point, puissance = 0, valeur, 0, 1


def afois():
    global operation, sauvegarde, valeur, point, puissance
    operation = "*"
    valeur, sauvegarde, point, puissance = 0, valeur, 0, 1


def adiv():
    global operation, sauvegarde, valeur, point, puissance
    operation = "/"
    valeur, sauvegarde, point, puissance = 0, valeur, 0, 1


def aegal():
    global operation, valeur, sauvegarde, puissance, point
    # Effectuer l'opération en fonction de la variable operation
    if operation == "+":
        resultat = sauvegarde + valeur
    elif operation == "-":
        resultat = sauvegarde - valeur
    elif operation == "*":
        resultat = sauvegarde * valeur
    elif operation == "/":
        if valeur == 0:
            resultat = "Erreur: division par zéro"
        else:
            resultat = sauvegarde / valeur
    else:
        resultat = valeur

    # Supprimer le .0 pour les résultats entiers
    if isinstance(resultat, float) and resultat.is_integer():
        resultat = int(resultat)

    # Afficher le résultat
    affichage.set(str(resultat))

    # Réinitialiser les variables pour la prochaine opération
    valeur = resultat
    sauvegarde = 0
    point = 0
    puissance = 1


def clear():
    global valeur, sauvegarde, puissance, point, affichage, operation
    valeur, sauvegarde, puissance = 0, 0, 1
    point, operation = 0, 0
    affichage.set("0.")


# création de la fenêtre
fenetre = Tk()
fenetre.title("Calculatrice")
fra1 = Frame(fenetre)
fra1.grid(row=1, column=0)
Button(fra1, text="9", command=x9, height=2, width=2).grid(
    row=2, column=2, padx=3, pady=3
)
Button(fra1, text="8", command=x8, height=2, width=2).grid(
    row=2, column=1, padx=3, pady=3
)
Button(fra1, text="7", command=x7, height=2, width=2).grid(
    row=2, column=0, padx=3, pady=3
)
Button(fra1, text="6", command=x6, height=2, width=2).grid(
    row=3, column=2, padx=3, pady=3
)
Button(fra1, text="5", command=x5, height=2, width=2).grid(
    row=3, column=1, padx=3, pady=3
)
Button(fra1, text="4", command=x4, height=2, width=2).grid(
    row=3, column=0, padx=3, pady=3
)
Button(fra1, text="3", command=x3, height=2, width=2).grid(
    row=4, column=2, padx=3, pady=3
)
Button(fra1, text="2", command=x2, height=2, width=2).grid(
    row=4, column=1, padx=3, pady=3
)
Button(fra1, text="1", command=x1, height=2, width=2).grid(
    row=4, column=0, padx=3, pady=3
)
Button(fra1, text="0", command=x0, height=2, width=2).grid(
    row=5, column=2, padx=3, pady=3
)
affichage = StringVar()
entree = Entry(fenetre, textvariable=affichage, bg="light yellow")
entree.grid(row=0, column=0)
affichage.set("0.")
Button(fra1, text="+", command=aplus).grid(row=2, column=5, padx=3, pady=3)
Button(fra1, text="-", command=amoins).grid(row=3, column=5, padx=3, pady=3)
Button(fra1, text="*", command=afois).grid(row=2, column=6, padx=3, pady=3)
Button(fra1, text="/", command=adiv).grid(row=3, column=6, padx=3, pady=3)
Button(fra1, text=".", command=virgule).grid(row=4, column=5, padx=3, pady=3)
Button(fra1, text="=", command=aegal).grid(row=4, column=6, padx=3, pady=3)
Button(fra1, text="C", command=clear).grid(row=5, column=6, padx=3, pady=3)
Button(fenetre, text="Quitter", command=fenetre.destroy).grid(row=6, column=7)
fenetre.mainloop()
