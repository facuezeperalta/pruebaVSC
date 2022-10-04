# funcion que recibe nombre y apellid y los agrega a un archivo
def AgregarDatos(nombre,apellido,dni):
    doc = open('Datos.txt','a')
    doc.write(nombre +' '+apellido +' '+dni +'\n')
    doc.close()



u1nombre = input('Ingrese el nombre del usuario: ')
u1apellido = input('Ingrese el apellido del usuario: ')
u1dni = input('Ingrese el DNI: ')


AgregarDatos(u1nombre,u1apellido,u1dni)