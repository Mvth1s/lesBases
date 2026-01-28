# Déclarer une variable avec un 'int' pour l'annotation de type
un_nombre: int = 32
un_nombre_a_virgule: float = 3.4

# Déclarer une variable avec une 'string' pour l'annotation de type
une_chaine_de_caractere: str = "Bonjour monde, ceci est une chaine de caractère !"

# Déclarer une foncion d'annotation de type avec des paramètres et des valeurs retournée
def ajouter_nombre (a: int, b:int) -> int:
    return a + b
    
print (ajouter_nombre(2,3))