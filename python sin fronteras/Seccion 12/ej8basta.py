# Ingresar numeros y con basta se corta la carga
lista = []
print('Ingrese numeros, para terminar escribra "basta"')

while True: 
    valor = input('Ingrese el valor: ')
    if valor == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except: 
            print('Dato ingresado inválido')
            exit()

resultado = 0

for x in lista:
    resultado += x

print('La cantidad de valores ingresados fue: ', len(lista))
print('La suma de los valores ingresados fue: ',resultado)