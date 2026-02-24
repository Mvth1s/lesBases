# -*- coding: utf-8 -*- #
from tkinter import *
fenetre = Tk()
fenetre.title('Dessin')
zone_dessin = Canvas(fenetre, width=500, height=500)
zone_dessin.create_line(0,0,500,500)
zone_dessin.create_rectangle(100,100,200,200)
zone_dessin.create_oval(300,200,350,250,width=2,fill='red')
zone_dessin.create_text(100,250,text="Exemple", fill='green', font=('Times', '34', 'bold italic'))
bouton=Button(fenetre, text='Quitter', command=fenetre.destroy)
zone_dessin.pack()
bouton.pack()
fenetre.mainloop()