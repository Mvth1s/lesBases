# -*- coding: utf-8 -*- #
from  tkinter import *
def  pointeur(event):
    chaine.configure (text="Clic détecté en X = "+str(event.x)+", Y = "+str(event.y))
fenetre=Tk()
cadre=Frame(fenetre, width=300, height=250, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine=Label(fenetre)
chaine.pack()
bouton=Button(fenetre, text='Quitter', command=fenetre.destroy)
bouton.pack()
fenetre.mainloop()