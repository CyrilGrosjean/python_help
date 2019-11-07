import time

a = 10
liste = ["Bonjour", "Comment", "Va"]
string = "Test"

for i in range(0, a):
    print(i)

time.sleep(5)

for i in liste:
    print(i)

time.sleep(5)

for a in string:
    print(a)

valide = True

while True:
    while valide:
        print("Valide est valide")
        valide = False
    print("Boucle infinie")
    time.sleep(1)