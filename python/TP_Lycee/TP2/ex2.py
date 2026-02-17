## ----------Utilisation d'une fonction---------- ##

from tkinter import Tk, Label, Button, LEFT, StringVar
from random import randint

# Fonction pour générer un nombre aléatoire
def hasard():
    nombre = randint(1, 6)
    Texte.set("Résultat -> " + str(nombre))
    
# Création de la fenêtre
fenetre = Tk()
fenetre.title("Dé à 6 faces")
fenetre.geometry("300x100+400+400")
boutonlancer = Button(fenetre, text = "Lancer", command = hasard)
boutonlancer.pack(side = LEFT, padx = 5, pady = 5)
Texte = StringVar()
hasard()
text = Label(fenetre, textvariable = Texte, fg = "blue", bg = "white")
text.pack(side = LEFT, padx = 5, pady = 5)
boutonquitter = Button(fenetre, text = "Quitter", command = fenetre.destroy)
boutonquitter.pack(side = LEFT, padx = 5, pady = 5)
fenetre.mainloop()