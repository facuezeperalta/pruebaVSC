from operator import truediv


def esPar(n):
    return n % 2 == 0

def esInpar(n):
    return n % 2 != 0

numero1 = int(input('Ingrese un numero para saber si es par o impar: '))
numero2 = int(input('Ingrese un numero para saber si es par o impar: '))


resultado1 = esPar(numero1)
resultado2 = esInpar(numero2)

if resultado1 == True: 
    print('El primer numero  es par')
else: print('El primer numero no es par')

if resultado2 == True:
    print('El segundo numero es impar')
else: print('El segundo numero es par')
