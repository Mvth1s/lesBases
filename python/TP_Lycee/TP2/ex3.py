## ----------Interaction avec l'utilisateur---------- ##

from tkinter import Tk, Label, Button, Entry, END

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

# ---------- autre ---------- #

def deg2kel(event):
    entre2.delete(0, END)
    valeur = eval(entre1.get())+273.15
    entre2.insert(0, valeur)
def kel2deg(event):
    entre1.delete(0, END)
    valeur = eval(entre2.get())-273.15
    entre1.insert(0, valeur)

fenetre = Tk()
fenetre.title("Convertisseur")
text1 = Label(fenetre, text = "Temperature en degrés :")
text2 = Label(fenetre, text = "Temperature en kelvin :")

entre1 = Entry(fenetre, bg="white")
entre1.bind("<Return>", deg2kel)
entre2 = Entry(fenetre, bg="white")
entre2.bind("<Return>", kel2deg)

bouton = Button(fenetre, text = "Quitter", command = fenetre.destroy)

text1.grid(row = 0)
text2.grid(row = 1)
entre1.grid(row = 0, column = 1)
entre2.grid(row = 1, column = 1)
bouton.grid(row = 2, column = 0)
fenetre.mainloop()