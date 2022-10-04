try:
    numero1 = int(input('Ingres el primer numero a sumar: '))

except:
    numero1 = 'Chanchito feliz'


try:
    numero2 = int(input('Ingrese el segundo numero a sumar: '))    

except: numero2 = 'Chanchito feliz'

if numero1 == 'Chanchito feliz' or numero2 == 'Chanchito feliz' :
    print('Ingresaste mal un dato proba de nuevo solo con números.')

else:
    print("La suma de los dos numeros ingresados es: ", numero1 + numero2)

