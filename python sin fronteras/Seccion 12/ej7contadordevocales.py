#Contar la cantidad de vocales que tiene una string
palabra = input('Ingrese su palabra: ')
contadorvocales = 0
contadorconsonantes = 0

for i in palabra:
    miniscula = i.lower()
    if miniscula == 'a' or miniscula == 'e' or miniscula == 'i' or miniscula == 'o' or miniscula == 'u':
        contadorvocales += 1
    else: 
        contadorconsonantes += 1

print('Cantidad de vocales: ',contadorvocales)
print('Cantidad de Consonantes: ',contadorconsonantes)


