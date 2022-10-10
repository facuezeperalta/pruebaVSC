from random import choice, sample
import os

mi_lista = [1,2,3,4,5,6,7,8,9,10]
dir(os)
print (choice(mi_lista))
print (sample(mi_lista,5)) #sample lleva el nombre de la lista + la cantidad de elementos a mostrar 
print (sample(mi_lista,10))


