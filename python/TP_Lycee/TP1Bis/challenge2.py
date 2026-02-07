#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Challenge 2: Calculer la factorielle d'un nombre sans utiliser le caractère '*' dans le code
"""


def main():

    print("----------Besoin n°6----------")
    print("Veillez choisir une nombre de départ !")
    nbr_depart = int(input())

    factoriel = 1
    for i in range(1, nbr_depart + 1):
        # Utilisation de la fonction mul pour éviter le caractère '*'
        factoriel = factoriel.__mul__(i)

    print("La factoriel de ", nbr_depart, " est : ", factoriel)


if __name__ == "__main__":
    main()
