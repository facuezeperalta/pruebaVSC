# Volumen de esfera por radio
def calcularvolumen(r):
    return 4/3 * 3.14 * r ** 3

radio = int(input('Ingrese el radio de la esfera para saber su volumen: '))

resultado = round(calcularvolumen(radio),3) # Funcion round para redondear los valores.

print(resultado)

