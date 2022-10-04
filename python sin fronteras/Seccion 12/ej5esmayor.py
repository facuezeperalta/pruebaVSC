#función que indique si el usario es mayor de edad.
def esMayor(usuario):
    return usuario.edad > 17


class Usuario():
    def __init__(self,edad):
        self.edad  = edad

usuario1 = Usuario(15)
usuario2 = Usuario(28)

resultadoU1 = esMayor(usuario1)
resultadoU2 = esMayor(usuario2)

print(resultadoU1)
print(resultadoU2)