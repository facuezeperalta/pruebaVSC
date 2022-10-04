class Usuario:#Clase
  def __init__(self,nombre, apellido):
      self.nombre = nombre
      self.apellido = apellido

  def saludo(self):
    print('Hola, mi nombre', self.nombre, self.apellido)

class Admin(Usuario): #le paso como atributo al método Usuario para que herede las cosas que tiene esa clase 
  def supersaludo(self):
    print('Hola me llamo', self.nombre, 'y soy admin papa.')

  

usuario = Usuario('Facundo','Peralta')
#usuario2 = Usuario('Roberto','Bolano')

usuario.saludo()

usuario.nombre = 'Roberto'

usuario.saludo ()

administrador = Admin('Super','Admin')

administrador.saludo()
administrador.supersaludo()







#print(usuario.nombre, usuario.apellido)
#print(usuario2.nombre,usuario2.apellido) 







