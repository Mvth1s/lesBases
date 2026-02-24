from tkinter import Button, Entry, Label, Tk


def repondre():
    affichage["text"] = reponse.get()


def repondre2():
    try:
        note = int(reponse2.get())
        affichage2["text"] = str(note)
        notefinal["text"] = str(note % 10)
    except:
        affichage2["text"] = "Erreur"


fenetre = Tk()
fenetre.title("Mon nom")

Label(fenetre, text="Quel est ton nom ?").pack()
reponse = Entry(fenetre)
reponse.pack()
Button(fenetre, text="Valider", command=repondre).pack()
Label(fenetre, text="Bonjour ").pack()
affichage = Label(fenetre, width=30)
affichage.pack()

Label(fenetre, text="Quelle est la note que tu voudrais avoir ?").pack()
reponse2 = Entry(fenetre)
reponse2.pack()
Button(fenetre, text="Valider", command=repondre2).pack()
Label(fenetre, text="même si tu pense avoir ").pack()
affichage2 = Label(fenetre, width=30)
affichage2.pack()
Label(fenetre, text="Je ne pense pas que tu puisse avoir plus de ").pack()
notefinal = Label(fenetre, text="")
notefinal.pack()
Label(fenetre, text="/20").pack()

Button(fenetre, text="Quitter", command=fenetre.destroy).pack()
fenetre.mainloop()
