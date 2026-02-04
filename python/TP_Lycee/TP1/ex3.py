
age = int(input("Quel est ton âge ?\n"))
if age > 10:
    print("tu as plus de 10 ans")
if age < 20:
    print("tu as moins de 20 ans")
if age != 18:
    print("tu n'es pas dans l'année de tes 18 ans")
if age == 18:
    print("tu es enfin majeur")
if age % 2:
    print("ton âge est un nombre impair")
else:
    print("ton âge est un nombre pair")
if age >= 18:
    print("tu peux signer tes absences tout seul")
elif age == 17:
    print("pas encore majeur, patience")
else:
    print("t'es encore un gamin")