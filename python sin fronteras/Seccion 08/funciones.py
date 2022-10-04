def mifuncion():
    print('Mi primera funcion')
    
#mifuncion()

def imprimedato(nombre,apellido):
    print('El nombre completo es:', nombre,apellido)

#imprimedato('Facundo','Peralta')


def miFuncionLista(lista):
    for elemento in lista:
        print(elemento)

#miFuncionLista(['Chanchito','Feliz'])

def concatenaNombres(lista2):
    i = ''
    for elemento in lista2:
        i = i + elemento + ' ' 
    return i


nombre = concatenaNombres(['Facundo','Peralta'])

print(nombre)


# recursividad

def recursion(i):
    if (i<1):
        return i 
    print(i)
    recursion(i -1)

 

