a = "10"
b = "Bonjour"

try:
    a = int(a)
    print("La str a peut être transformée en int")
except:
    print("A ne peut pas être transformé en int")

try:
    b = int(b)
    print("B est un nombre entier")
except:
    print("B n'est pas un nombre")