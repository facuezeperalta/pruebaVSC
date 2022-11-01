import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user= 'root',
    password = '1623',
    database = 'prueba2',
    port = '3306',
)
cursor = conexion.cursor() #cursor es un objeto que nos permite
#interactuar con la BD mediante instruacciones SQL.


#cursor.execute('select * from Usuario') para elegir desde la tabla.


sql = 'insert into Usuario (emial,username,edad) values (%s,%s,%s)'
values = ('facundo@gmail.com', 'usuarioPython',27)

cursor.execute(sql,values)

#ver que tiene mi modelo de base de datos
#cursor.execute('show create table Usuario')
resultado = cursor.fetchall() #devuelve todas las
# insntacias que encontró en la base de datos fectchone devuelve el primero que encontró.

print (resultado)

