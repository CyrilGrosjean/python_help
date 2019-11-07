liste = ["1", "2", "3", "4", "5"]
dictionnaire = {"Marches": 32, "Escaliers": 4}

print(liste)
print(dictionnaire)

liste[2] = "6"
print(liste)
print("Index du 6:" liste.index("6"))

dictionnaire["Marches"] = 40
print(dictionnaire)
print("Nombre de marches: " + str(dictionnaire.get("Marches")))

liste_join = "\n".join(liste)
print("Liste jointe: "+liste_join)

print("Liste reverse:")
print(liste.reverse())