# defino la función 
def creacionUsario(nombre,dni,edad,sexo):
    documento = open('Datos2.txt','a')
    documento.write('Nombre: '+nombre + ',' +' '+ 'DNI: '+ dni + ',' +' '+'Edad: '+ edad +',' + ' ' + 'Sexo: '+ sexo + '.'+ '\n')
    documento.close()
#inicializo las variables
nombre = '' 
dni = ''
edad = '' 
sexo = ''
print('Carga de usuarios, para acabar ingrese "done" en el campo de nombre')

while True: 
    print('------')
    nombre = input('Ingrese el nombre del usuario: ')
    if nombre == 'done':
        print('Carga finalizada')
        break
    else:
        try:
            apellido = input('Ingrese el apellido del usuario: ')
            edad = input('Ingrese la edad del usuario: ')
            sexo = input('Ingrese el sexo del ususario: ')
            creacionUsario(nombre,apellido,edad,sexo)
        except: 'Error inesperado por favor contacte con un administrador.'

        

    


