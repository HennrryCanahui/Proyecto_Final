from Conector import conexion
import random
cursor = conexion.cursor()
def generar_numero_unico(cursor):
    while True:
        numero_generado = random.randint(1000, 9999)  # generador del identifiacor en un rango de 4 digitos
        if not verificar_numero(numero_generado, cursor):
            return numero_generado

def verificar_numero(numero, cursor):
    query = "SELECT * FROM pruebas_1 WHERE Identificacion = %s"
    cursor.execute(query, (numero,))
    return cursor.fetchone() is not None


# variable de almacenamieto del numero generado 

"""numero_a_verificar = generar_numero_unico(cursor)"""

# testeo que si funciono el numeor genrado

"""print(numero_a_verificar)"""