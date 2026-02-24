# -*- coding: utf-8 -*- #
from tkinter import * 

couleur="#001100"

def change_couleur(event):#fonction qui récupère les valeurs des slider et les traite
    rouge_hex=hex(int(Valeur_rouge.get()))
    vert_hex=hex(int(Valeur_vert.get()))
    bleu_hex=hex(int(Valeur_bleu.get()))
    rouge_hex=rouge_hex[2:4]
    vert_hex=vert_hex[2:4]
    bleu_hex=bleu_hex[2:4]
    if len(rouge_hex)<2:
        rouge_hex="0"+rouge_hex
    if len(vert_hex)<2:
        vert_hex="0"+vert_hex
    if len(bleu_hex)<2:
        bleu_hex="0"+bleu_hex
    couleur="#"+rouge_hex+vert_hex+bleu_hex
    Dessin['bg']=couleur
    Label_couleur['text']="couleur en hexadécimal : "+couleur
    chaine_couleur=couleur

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Mélange_Couleurs')
Mafenetre.geometry('630x420+300+300')
Mafenetre.config(background="grey")

# Création d'un widget Label (texte 'titre de la fenetre : Mélangeur de couleurs')
Label1 = Label(Mafenetre, text = 'Mélangeur de couleurs',  fg = 'red',font="Calibri 16 bold")
Label1.grid(row=0, column=0, columnspan=3,sticky='ew') #occupation de toute la largeur avec sticky=ew

# Création des widget Scale (Potentiomètre horizontal)
Valeur_rouge = StringVar()
Valeur_rouge.set(30)
rouge=Scale(Mafenetre, orient='horizontal', from_=0, to=254,
      resolution=15, tickinterval=10, length=510,variable=Valeur_rouge,
      label='Rouge',bg='red',fg = 'white',font="Calibri 12 bold",troughcolor='pink')
rouge.grid(row=1,column=0,pady=5)

Valeur_vert = StringVar()
Valeur_vert.set(45)
vert=Scale(Mafenetre, orient='horizontal', from_=0, to=254,
      resolution=15, tickinterval=10, length=510,variable=Valeur_vert,
      label='Vert',bg='green',fg = 'white',font="Calibri 12 bold",troughcolor='pink')
vert.grid(row=2,column=0,pady=5)

Valeur_bleu = StringVar()
Valeur_bleu.set(45)
bleu=Scale(Mafenetre, orient='horizontal', from_=0, to=254,
      resolution=15, tickinterval=10, length=510,variable=Valeur_bleu,
      label='Bleu',bg='blue',fg = 'white',font="Calibri 12 bold",troughcolor='pink')
bleu.grid(row=3,column=0,pady=5)

# Création d'un widget Canvas pour la zone à colorier
Dessin = Canvas(Mafenetre, width = 100, height =200, bg =couleur)
Dessin.grid(row=1,column=2,rowspan=3,sticky='ewns',pady=5,padx=5)

# Création d'un widget Label (texte 'couleur en hexadécimal :')
Label_couleur = Label(Mafenetre, text = 'chaine_couleur', bg='grey', fg = 'white',font="Calibri 24 bold")
Label_couleur.grid(row=4, column=0, columnspan=3,sticky='ew') #occupation de toute la largeur avec sticky=ew

# Création d'un widget Label (texte 'sti2d sin isn')
Label_site = Label(Mafenetre, text = 'STI2D SIN', bg='grey', fg = 'blue',font="Dungeon 22 bold")
Label_site.grid(row=5, column=0, columnspan=3,sticky='ew')

# Création des evènements
rouge.bind('<Motion>',change_couleur) #Motion pour mvt de souris dans le widget
vert.bind('<Motion>',change_couleur)
bleu.bind('<Motion>',change_couleur)

# Lancement du gestionnaire d'événements
Mafenetre.mainloop()