"""from Conexion.Conexion import *
import random
cursor = conexion.cursor()
def generar_numero_unico(cursor):
    while True:
        numero_generado = random.randint(100, 999)  # Puedes ajustar el rango según tus necesidades
        if not verificar_numero(numero_generado, cursor):
            return numero_generado

def verificar_numero(numero, cursor):
    query = "SELECT * FROM pruebas_1 WHERE Identificacion = %s"
    cursor.execute(query, (numero,))
    return cursor.fetchone() is not None


# Guarda el numero identificador
numero_a_verificar = generar_numero_unico(cursor)
print(numero_a_verificar)"""
