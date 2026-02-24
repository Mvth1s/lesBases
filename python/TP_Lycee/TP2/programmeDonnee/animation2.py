# -*- coding: utf-8 -*- #
from tkinter import*
def move():
	global x1, y1, dx, dy, flag
	x1, y1 = x1+dx, y1+dy
	if x1>210 :
		x1, dx, dy = 210, 0, 15
	if y1>210:
		y1, dx, dy = 210, -15, 0
	if x1<10:
		x1, dx, dy = 10, 0, -15
	if y1<10:
		y1, dx, dy = 10, 15, 0
	canevas.coords(baballe,x1,y1,x1+30,y1+30)
	if flag>0:
		fenetre.after(50,move) 
def stop_it():
	global flag
	flag=0
def start_it():
	global flag
	if flag==0:
		flag=1
		move()

x1, y1 = 10, 10
dx, dy = 15, 0 
flag=0 
fenetre=Tk()
fenetre.title("Animation auto")
canevas=Canvas(fenetre,bg='dark gray',height=250, width=250)
canevas.pack(side=LEFT,padx=5,pady=5)
baballe=canevas.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
boutonquitter=Button(fenetre,text='Quitter',width=8,command=fenetre.destroy)
boutonquitter.pack(side=BOTTOM)
boutondemarrer = Button(fenetre,text='Demarrer',width=8,command=start_it)
boutondemarrer.pack()
boutonarreter = Button(fenetre,text='Arreter',width=8,command=stop_it)
boutonarreter.pack()
fenetre.mainloop()
fenetre.destroy()