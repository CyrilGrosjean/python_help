nombre = 0

def ajoute_1(nombre):
    nombre += 1
    return nombre

def variable_locale():
    k = 1

def variable_globale():
    global nombre
    nombre += 2

print(nombre)
nombre = ajoute_1(nombre)
print(nombre)
variable_locale()
try:
    print(k)
except:
    pass
variable_globale()
print(nombre)