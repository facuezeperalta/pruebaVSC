
print('Me gusta ser un modulo')
print(__name__)


# codigos defino funciones.
__contador = 0

def suml(lista):
    global __contador
    __contador += 1
    
    la_suma = 0 

    for elemento in lista:
        la_suma += elemento
        return la_suma

def prod1(lista):
    global __contador
    __contador +=1 
    prod = 1 
    for elemento in lista:
        prod *= elemento
    
    return prod


if __name__ == "__main__":
    print('Yo prefiero ser un modulo, pero puedo realizar algunas pruebas para vos')

    mi_lista =[i+1 for i in range(5)]
    print(suml(mi_lista) == 15)
    print(prod1(mi_lista) == 120) 