import random

valide = True
a = random.randint(0, 2)
liste = ["Bonjour", "Comment", "Va"]

if valide:
    print("Bonjour")

if "Va" in liste:
    print("\"Va\" est dans la liste")

if a == 1:
    print("A vaut 1")
elif a == 2:
    print("A vaut 2")
else:
    print("A vaut 3")

valide = False

if not valide:
    print("Valide n'est pas valide lol")