# -*- coding: utf-8 -*- #
from tkinter import*
def avance(gd, hb):
	global x1, y1
	x1, y1 = x1+gd, y1+hb
	canevas.coords(baballe, x1, y1, x1+30, y1+30)
def depl_gauche():
	avance(-10, 0)
def depl_droite():
	avance(10, 0)
def depl_haut():
	avance(0, -10)
def depl_bas():
	avance(0, 10)
x1, y1 = 10, 10 
fenetre = Tk()
fenetre.title("Animation")
canevas = Canvas(fenetre, bg='dark gray', height=300, width=300)
baballe=canevas.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
canevas.pack(side=LEFT)
Button(fenetre,text='Quitter',command=fenetre.quit).pack(side=BOTTOM)
Button(fenetre,text='Gauche',command=depl_gauche).pack()
Button(fenetre,text='Droite',command=depl_droite).pack()
Button(fenetre,text='Haut',command=depl_haut).pack()
Button(fenetre,text='Bas',command=depl_bas).pack()
fenetre.mainloop()
fenetre.destroy()