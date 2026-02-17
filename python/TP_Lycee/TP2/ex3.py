## ----------Interaction avec l'utilisateur---------- ##

from tkinter import Tk, Label, Button, Entry

def repondre():
    affichage['text'] = reponse.get()

fenetre = Tk()
fenetre.title("Mon nom")
nom = Label(fenetre, text = "Votre nom :")
reponse = Entry(fenetre)
boutonvalider = Button(fenetre, text = "Valider", command = repondre)
affichage = Label(fenetre, width = 30)
votre_nom = Label(fenetre, text = "Votre nom est :")
boutonquitter = Button(fenetre, text = "Quitter", command = fenetre.destroy)
nom.pack()
reponse.pack()
boutonvalider.pack()
votre_nom.pack()
affichage.pack()
boutonquitter.pack()
fenetre.mainloop()