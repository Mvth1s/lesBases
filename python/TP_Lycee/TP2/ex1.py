## ----------Première Interface---------- ##

from tkinter import Tk, Label, Button

# ----------- Part 1 ---------- #

fenetre = Tk()
fenetre.title('Coucou')
texte = Label(fenetre, text = 'Bonjour tout le monde !', fg = 'red')
texte.pack()
bouton = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
bouton.pack()
fenetre.mainloop()
 
# ----------- Part 2 ---------- #

fenetre = Tk()
fenetre.title('Coucou')
texte = Label(fenetre, text = 'Bonjour tout le monde !', fg = 'red')
texte.pack()
texte2 = Label(fenetre, text = 'Comment ça va ?', fg = '#0000FF')
texte2.pack()
bouton = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
bouton.pack()
fenetre.mainloop()

# ----------- Part 3 ---------- #

fenetre = Tk()
fenetre.title("Part 3")
texte = Label(fenetre, text = "Hello Python !", fg = "#10b981")
texte.pack()
texte2 = Label(fenetre, text = "Les bases de Python d'après mes cours de Lycée !")
texte2.pack()
bouton = Button(fenetre, text = "Quitter", command = fenetre.destroy)
bouton.pack()
fenetre.mainloop()