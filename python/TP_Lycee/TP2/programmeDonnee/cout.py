# -*- coding: utf-8 -*- #
from tkinter import *

def calculer():
    px=float(p.get())
    masse=float(m.get())
    total=str(round(px*(masse/1000),2))
    # Création d'un widget Label (texte 'coût estimé')
    Label_resultat = Label(Mafenetre, text = 'Coût matière estimé : '+str(total)+" €", font="'arial',15,bold",bg='pink',fg = 'blue')
    # Positionnement du widget avec la méthode grid()
    Label_resultat.grid(row=5, column=0,columnspan=2)

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Cout impression')
Mafenetre.geometry('233x150+300+300')
Mafenetre.config(background="light grey")

# Création d'un widget Label (texte 'titre de la fenetre : Calculateur de coût d\'impression 3d')
Label1 = Label(Mafenetre, text = 'Calculateur de coût d\'impression 3d',  fg = 'black')
Label1.grid(row=0, column=0, columnspan=2,sticky='ew') #occupation de toute la largeur avec sticky=ew

# Création d'un widget Label (texte 'demande prix')
Label_demandeprix = Label(Mafenetre, text = 'Prix au kilo en €', bg='light grey',fg = 'black')
Label_demandeprix.grid(row=2, column=0)

# Création d'un widget Entry (champ de saisie pour le prix d'achat de la bobine)
p=StringVar()
zone1 = Entry(Mafenetre, textvariable= p, bg ='yellow', fg='maroon')
zone1.grid(row=2, column=1)

# Création d'un widget Label (texte 'demande masse estimée')
Label_demandemasse = Label(Mafenetre, text = 'Masse estimée en g', bg='light grey',fg = 'black')
Label_demandemasse.grid(row=3, column=0)

# Création d'un widget Entry (champ de saisie)
m=StringVar()
zone2 = Entry(Mafenetre, textvariable= m, bg ='yellow', fg='maroon')
zone2.grid(row=3, column=1)

# Création d'un widget Button (bouton calcul)
Bouton_calcul = Button(Mafenetre, text = 'Calcul', command = calculer) #envoi vers la fonction calcul
Bouton_calcul.grid(row=4, column=0,columnspan=2)

# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)
Bouton1.grid(row=6, column=0,columnspan=2)

# Lancement du gestionnaire d'événements
Mafenetre.mainloop()
