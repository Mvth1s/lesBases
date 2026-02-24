# -*- coding: utf-8 -*- #
from tkinter import *

def convert_bin_hex():
    decimal=int(dec.get())
    bina.set(str(bin(decimal)))
    hexa.set(str(hex(decimal)))

def convert_dec_hex():
    binaire=int(bina.get(),2)
    dec.set(str(int(binaire)))
    hexa.set(str(hex(binaire)))

def convert_dec_bin():
    hexadec=int(hexa.get(),16)
    dec.set(str(int(hexadec)))
    bina.set(str(bin(hexadec)))

def efface_dec():dec.set('')
def efface_bin():bina.set('')
def efface_hex():hexa.set('')

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Convertisseur')
Mafenetre.geometry('234x170+300+300')
Mafenetre.config(background="grey")

# Création d'un widget Label (texte 'titre de la fenetre : Convertisseur décimal-binaire-hexadécimal')
Label1 = Label(Mafenetre, text = 'Convertisseur décimal-binaire-hexadécimal', fg = 'blue')
Label1.grid(row=0, column=0,columnspan=3) #occupation de toute la largeur avec sticky=ew

# Création d'un widget Entry (champ de saisie pour le nombre en décimal à convertir)
dec=StringVar()
zone1 = Entry(Mafenetre, textvariable= dec, bg ='yellow', fg='maroon')
zone1.grid(row=2, column=0,pady=5)
dec.set('valeur décimale')

# Création d'un widget Entry (champ de saisie pour le nombre en binaire à convertir)
bina=StringVar()
zone2 = Entry(Mafenetre, textvariable= bina, bg ='yellow', fg='maroon')
zone2.grid(row=3, column=0,pady=5)
bina.set('valeur binaire')

# Création d'un widget Entry (champ de saisie pour le nombre en hexadécimal à convertir)
hexa=StringVar()
zone3 = Entry(Mafenetre, textvariable= hexa, bg ='yellow', fg='maroon')
zone3.grid(row=4, column=0,pady=5)
hexa.set('valeur hexadécimale')

# Création d'un widget Button (bouton convertir)
Bouton_calcul = Button(Mafenetre, text = 'convertir',command=convert_bin_hex) #envoi vers la fonction decimal vers binaire et hexa
Bouton_calcul.grid(row=2, column=2,pady=2)

# Création d'un widget Button (bouton convertir)
Bouton_calcul1 = Button(Mafenetre, text = 'convertir',command=convert_dec_hex) #envoi vers la fonction binaire vers décimal et hexa
Bouton_calcul1.grid(row=3, column=2,pady=2)

# Création d'un widget Button (bouton convertir)
Bouton_calcul2 = Button(Mafenetre, text = 'convertir',command=convert_dec_bin) #envoi vers la fonction hexa vers décimal et binaire
Bouton_calcul2.grid(row=4, column=2,pady=2)

# Création d'un widget Button (bouton efface)
Bouton_efface = Button(Mafenetre, text = 'DEL',command=efface_dec) #envoi vers la fonction hexa vers décimal et binaire
Bouton_efface.grid(row=2, column=1,pady=2)

# Création d'un widget Button (bouton efface)
Bouton_efface1 = Button(Mafenetre, text = 'DEL',command=efface_bin) #envoi vers la fonction hexa vers décimal et binaire
Bouton_efface1.grid(row=3, column=1,pady=2)

# Création d'un widget Button (bouton efface)
Bouton_efface2 = Button(Mafenetre, text = 'DEL',command=efface_hex) #envoi vers la fonction hexa vers décimal et binaire
Bouton_efface2.grid(row=4, column=1,pady=2)

# Création d'un widget Button (bouton Quitter)
Bouton1 = Button(Mafenetre, text = 'Quitter', command = Mafenetre.destroy)
Bouton1.grid(row=6, column=0,columnspan=3, pady=5)

# Lancement du gestionnaire d'événements
Mafenetre.mainloop()