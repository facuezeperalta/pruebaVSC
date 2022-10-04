# para borrar tenemos que importar un modulo del sistema.
import os #OS importa comandos para eliminar y modificar archivos.

if os.path.exists('e:/workspace/Seccion 11/asdf.txt'):
    os.remove('e:/workspace/Seccion 11/asdf.txt')
    print('El archivo se ha removido correctamente.')
else: print('No se ha encontrado el archivo...')


   


