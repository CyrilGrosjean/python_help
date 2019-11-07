integer = 3
flottant = 5.13
chaine = "Bonjour"
caractere = "O"
liste = ["Comment", "Allez", "Vous"]
liste_complexe = ["Salut", "Comment", 46, ["Bonjour", "Au revoir"]]
dictionnaire = {"Marches": 150, "Prénom": "Caroline"}

print("Un texte")
print(integer)
print(flottant)
print("Chaine: "+chaine)
print("Nombre: "+str(integer))
print("Liste:", liste)
print("Un élément de la liste: "+str(liste[1]))
print("Element liste complexe: ", liste[3])
print("Element d'un élement liste: "+str(liste[3][1]))
print("Dictionnaire: ", dictionnaire)
print("Element dictionnaire: "+str(dictionnaire.get("Marches")))