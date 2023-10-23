import flet as ft
import mysql.connector
from datetime import datetime

def establecer_conexion():
    
    #Función para establecer una conexión a la base de datos MySQL.
    try:
        conexion = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="enty",
            port="3306"
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            print("")
            return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")

def obtener_fecha_hora_actual():
        now = datetime.now()
        fecha_actual = now.strftime("%d/%m/%Y")
        hora_actual = now.strftime("%I:%M:%S %p")
        return fecha_actual, hora_actual

def Entradas(page: ft.Page):

    # Establecer conexión a la base de datos
    conexion = establecer_conexion()

    page.appbar = ft.AppBar(
        title=ft.Text("Registro Entrada"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    def Existencia_id(conexion):
        id_empleado = Empleado.value
        query = "SELECT * FROM registros WHERE ID = %s AND fecha_entrada = CURDATE() AND (hora_salida IS NULL OR hora_salida = '')"
    
        with conexion.cursor() as cursor:
            cursor.execute(query, (id_empleado,))
            result = cursor.fetchone()

        if result is not None:
        # La identificación existe y hay un registro con la hora de salida vacía, continuar con normalidad
            return True
        else:
        # La identificación no existe o ya hay un registro con la hora de salida, mostrar alerta
            alerta = ft.AlertDialog(
                title=ft.Text("Registro Existente"),
                content=ft.Text("Ya existe un registro para este ID y fecha de entrada con hora de salida."),
            )
            page.dialog = alerta
            alerta.open = True
            page.update()
            return False
        
    def button_clicked(e):
        
        if not Existencia_id(conexion):
            # La identificación no existe, no continuar con el proceso
            return
    
        """fecha_actual, hora_entrada = obtener_fecha_hora_actual()

        # Resto del código para la inserción en la base de datos
        sql = "INSERT INTO registros (fecha_entrada, hora_salida) VALUES (%s, %s)"
        val = (Empleado.value, fecha_actual, hora_entrada,)

        with conexion.cursor() as cursor:
            cursor.execute(sql, val)
            conexion.commit()
            print(cursor.rowcount, "record inserted.")"""

    
    
     # Crear elementos de la interfaz de usuario
    Empleado = ft.TextField(label="Nombres")
    Validacion = ft.ElevatedButton(text="Registrar", on_click=button_clicked)
    
    row_1 = ft.Row(controls=[
        ft.Container(expand=1),
        ft.Container(Empleado, expand=1),
        ft.Container(expand=1),
    ])

    row_2 = ft.Row(controls=[
        ft.Container(expand=1),
        ft.Container(Validacion, expand=1),
        ft.Container(expand=1),
    ])
    

ft.app(target=Entradas)