# Multiplicar dos numeros sin usar el simbolo *
from unittest import result


a = int(input('Ingrese el primero número: '))
b = int(input('Ingrese el segundo número: '))
resultado = 0

for x in range(a):
    resultado += b

print(resultado)

