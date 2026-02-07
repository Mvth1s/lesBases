#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Challenge 1: Afficher un sapin avec des astérisques sans utiliser le caractère '*' dans le code
"""


def main():
    # Utilisation du code ASCII 42 pour obtenir le caractère '*'
    asterisk = chr(42)

    # Fonction pour répéter un caractère sans utiliser '*'
    def repeat_char(char, count):
        result = ""
        for _ in range(count):
            result += char
        return result

    # Construction du sapin ligne par ligne
    sapin = [
        asterisk,
        repeat_char(asterisk, 3),
        repeat_char(asterisk, 5),
        repeat_char(asterisk, 5),
        repeat_char(asterisk, 7),
        repeat_char(asterisk, 9),
        repeat_char(asterisk, 11),
        asterisk,
        asterisk,
        repeat_char(asterisk, 3),
    ]

    # Largeur maximale pour le centrage (longueur de la ligne la plus longue)
    largeur_max = 11

    # Affichage du sapin avec centrage
    for ligne in sapin:
        print(ligne.center(largeur_max))


if __name__ == "__main__":
    main()
