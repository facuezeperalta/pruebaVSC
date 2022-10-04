try:
    numero1 = int(input('Ingrese el primero numero:'))
except: 
    numero1 = 'error'
if numero1 == 'error':
    print('El valor ingresado no es un numero.')
try: 
    numero2 = int(input('Ingrese el segundo numero: '))

except:
    numero2 = 'error' 
if numero2 == 'error':
    print('El valor ingresado no es número')

print('----------')

simbol = input('Ingrese la operación a realizar (+,-,*,/): ')

if simbol == '+':
    print('Resultado de la suma',numero1 + numero2)

elif simbol == '-':
    print('Resultado de la resta:', numero1 - numero2)

elif simbol == '*':
    print('Resultado de la multiplación: ',numero1 * numero2)

elif simbol == '/':
    print('Resultado de la división: ', numero1 / numero2)

else: print('La operación ingresada no esta soportada.')
     

