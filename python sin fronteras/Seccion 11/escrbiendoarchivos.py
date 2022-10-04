#abrimos el archivo
from cgitb import text


texto = open('e:\workspace\Seccion 11\Foto.txt','a')

texto.write('\nAgregue una linea de texto para meter mas cosas.')

texto.close()

x = open('e:\workspace\Seccion 11\Foto.txt')

print(x.read())

