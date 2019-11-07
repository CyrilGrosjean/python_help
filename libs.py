import math
from random import randint
from sys import *
import time

print("Exemple math")
a = 3
b = 2
resultat = math.pow(a, b)
print("3^2 = "+str(resultat))
del a, b, resultat

time.sleep(3)

print("Exemple random")
resultat = randint(1,10)
print(resultat)

time.sleep(3)

print("Exemple sys")
exit(84)