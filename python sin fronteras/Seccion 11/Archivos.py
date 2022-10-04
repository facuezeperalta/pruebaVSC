text = open('e:\workspace\Seccion 11\Foto.txt')
#print(text.read()) #imprime todo el archivo solicitado.
#print(text.readline())#Imprime linea por linea si lo repito imprime la que sigue.
for linea in text:
    print(linea)

text.close()


#print(text.read())  Si intento ejecutar el comando de imprimir todo el archivo luego de cerrarlo
# me generá un error.

