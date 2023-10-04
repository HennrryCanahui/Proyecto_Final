import random
from .Conector import conexion

def generar_numero_unico():
    while True:
        numero_generado = random.randint(1000, 9999)
        if not verificar_numero(numero_generado, conexion):
            return numero_generado

def verificar_numero(numero, cursor):
    query = "SELECT * FROM pruebas_1 WHERE Identificacion = %s"
    with cursor.cursor() as cursor:
        cursor.execute(query, (numero,))
        return cursor.fetchone() is not None


