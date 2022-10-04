class Producto:
    Codigo = 0
    Nombre = ''
    Precio = 0

    def __init__(self, codigo, nombre, precio):
        self.Codigo = codigo
        self.Nombre = nombre
        self.Precio = precio
    
    def get_Codigo(self):
        return self.Codigo
    
    def set_Codigo(self, codigo):
        self.Codigo = codigo
    
    def get_Nombre(self):
        return self.Nombre
    
    def set_Nombre(self,nombre):
        self.Nombre = nombre
    
    def get_Precio(self):
        return self.Precio

    def set_Precio(self, precio):   
        self.Precio = precio
    
    def __str__(self):
        return ('El código del producto es: '+ str(self.Codigo) + 'Su nombre es:  '+ str(self.Nombre) +
        'El precio del producto es: ' + str(self.Precio))
    
    def descripcion_producto(self,nombre,codigo,precio):
        return ('El nombre del producto: ',self.Nombre, 'El codigo: ',
        self.Codigo, 'El precio es: ', self.Precio)
    
    def calcular_total(self, unidades):
       # capturo todo en un print: print('El total de lo pedido es: '+ str(self.Precio * unidades)) 
       return ('El total del pedido es: ' + str(self.Precio * unidades))
    

miPrimeroProducto = Producto #Creo mi objeto.

miPrimeroProducto.Codigo = 15
miPrimeroProducto.Nombre = 'iPhone 14 Pro max'
miPrimeroProducto.Precio = 1300

resultado = miPrimeroProducto.calcular_total(miPrimeroProducto,2)

print(resultado)

miPrimeroProducto.descripcion_producto




















    




    

    
