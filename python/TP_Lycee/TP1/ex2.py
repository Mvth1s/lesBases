
nom = input("Quel est ton nom ?\n")
print("Bonjour", nom, " !")
note = input("Quelle est la note que tu voudrais avoir ?\n")
print("même si tu pense avoir ", note)
reponse = "Je ne pense pas que tu puisse avoir plus de " + str(int(note) % 10) + "/20 !"
print(reponse)