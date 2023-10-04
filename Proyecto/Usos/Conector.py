import mysql.connector

    # Intenta establecer la conexión
conexion = mysql.connector.connect(
    user="Enty",
    password="",
    host="localhost",
    database="enty",
    port="3306"
)



    # Si la conexión se establece correctamente, imprime un mensaje
if conexion.is_connected():
    print("Conexión exitosa a la base de datos.")

