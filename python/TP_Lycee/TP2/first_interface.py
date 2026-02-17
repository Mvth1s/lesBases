from tkinter import Tk, Label, Button

fenetre = Tk()
fenetre.title('Coucou')
texte = Label(fenetre, text = 'Bonjour tout le monde !', fg = 'red')
texte.pack()
bouton = Button(fenetre, text = 'Quitter', command = fenetre.destroy)
bouton.pack
fenetre.mainloop()