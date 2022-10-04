try:
    numero1 = int(input("Ingrese el primer numero: "))
except:
    numero1 = 'Chanchito feliz'

if numero1 == 'Chanchito feliz':
    print('El valor ingresado no es un número')
    exit()

try: 
    numero2 = int(input('Ingrese el segundo número: '))
except:
    numero2 = 'Chanchito feliz'

if numero2 == 'Chanchito feliz':
    print('El valor ingresado no es un número')
    exit()

print(numero1 + numero2)


