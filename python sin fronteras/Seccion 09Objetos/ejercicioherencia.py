# Crear clase de gato.
# Crear clase de perro.
class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola soy un ',self.tipo,'y mi onomatopeya es',self.onomatopeya)
    
    def saludofeminio(self):
        print('Hola soy una',self.tipo,'y mi onomatopeya es', self.onomatopeya )
    

        
class Gato(Animal):
   tipo = 'gato' 
   def __init__(self,nombre,onomatopeya): #forma uno de extender metodo init de la clas padre
    Animal.__init__(self,nombre,onomatopeya)
    print('Hola soy un gato extendido')


class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):#segunda forma de extender el método init
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro')

class Lora(Animal):
    tipo = 'lora'

class Tortuga(Animal):
    tipo = 'tortuga'

class Pavo(Animal):
    tipo = 'pavo'

gato = Gato('Nexus','Maullido')
gato.saludo()

perro = Perro('Ringo','Ladrido')
perro.saludo()

lora = Lora('Pepe','Parloteo')

lora.saludofeminio()

tortuga = Tortuga('Burn','no tengo')
tortuga.saludofeminio()

pavo = Pavo('Reali','Vocear')
pavo.saludo()








        

        
