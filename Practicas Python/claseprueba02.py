
class pedido:
    Producto = []
    Cantidades = []

    #defino metodo constructor
    def __init__(self):
        self.Producto = []
        self.Cantidades = []
    
    def agregarproducto(self,producto,cantidad):
        if not isinstance(producto,producto):
            #raise sirve para lanzar de manera intencionada excepciones en nuestro código.
            raise Exception('agregar producto debe ser de la clase Producto')
        
        if not isinstance(cantidad,int):
            raise Exception('Agregar producto Cantidades debe ser un número')
        
        if cantidad < 0:
            raise Exception ('Agregar producto debe ser mayor a 0')
        

        
        



        


