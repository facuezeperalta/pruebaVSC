from modulos import saludo, mascotas # sirve para importar un modulo con otro nombre as xs
# from deja importar desde modulos solo la funcion que quiero
from camelcase import CamelCase
c = CamelCase()
s = 'esta oración necesita CamelCase'

#print(modulos.mascotas)
print(mascotas) # Acá ejecuta solamenta la función mascotas sin necesidar de anteponer
# modulos.mascostas, se ejecuta derecho.

nombreparasaludar = input('Ingrese su nombre: ')    

saludo(nombreparasaludar)

camelcased = c.hump(s)

print(camelcased)



 









