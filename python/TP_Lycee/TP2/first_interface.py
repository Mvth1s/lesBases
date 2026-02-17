from tkinter import Tk, Label, Button

# ----------- Part 1 ---------- #

fenetre = Tk()
fenetre.title('Coucou')
texte = Label(fenetre, text = 'Bonjour tout le monde !', fg = 'red')
texte.pack()
bouton = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
bouton.pack
fenetre.mainloop()
 
# ----------- Part 2 ---------- #

fenetre = Tk()
fenetre.title('Coucou')
texte = Label(fenetre, text = 'Bonjour tout le monde !', fg = 'red')
texte.pack()
texte2 = Label(fenetre, text = 'Comment ça va ?', fg = '#0000FF')
texte2.pack()
bouton = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
bouton.pack
fenetre.mainloop()
