# Encontrar el menor elemento de una lista
#Creo la lista vacia
from re import M


lista2 = []
control = 0

print('---------')
numero = int(input('Ingrese un numero a la lista, -9999 termina la carga: '))

while control != -9999:
    numero = int(input('Ingrese el numero proximo a agregra a la lista, -9999 termina la carga: '))
    control = numero
    lista2.append(numero)
    
print('Carga finalizada con éxito...')
print('El tamaño de la lista cargada es de: ',len(lista2))

numeromenor = lista2[0]
numeromayor = lista2[0]

opcion = input('Ingrese a para ver el menor y b para ver el mayor de la lista: ')

if opcion == 'a':
    for me in lista2:
        if me < numeromenor:
            numeromenor = me
elif opcion == 'b':
    for ma in lista2:
        if ma > numeromayor:
            numeromayor = ma

else: 'Opción ingresada incorrecta' 

print('El numero menor es: ', numeromenor)
print('El numero mayor es: ', numeromayor)


#lista = [1,2,5,8,14,-10,25,-50,-30,100,50,40,500]
#mayor = lista[0]
#menor = lista[0]

#for m in lista: #busco al mayor de la lista
   # if mayor > m:
       # continue
   # else:
        #mayor = m 

#for c in lista:
    #if menor < c:
     #   continue
    #else: 
     #   menor = c


#print('El mayor es: ', mayor)
#print ('El menor es:',menor)


