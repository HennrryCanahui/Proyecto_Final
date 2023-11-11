import flet as ft
import mysql.connector
from datetime import datetime

#Función para establecer una conexión a la base de datos MySQL.
def establecer_conexion():
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

def Entradas(page: ft.Page):

    # verifica si el id existe o no 
    def Existencia_id(conexion):
        id_empleado = Empleado.value  # Obtén el valor de Empleado.value
        query = "SELECT * FROM empleados WHERE Identificación = %s"
        with conexion.cursor() as cursor:
            cursor.execute(query, (id_empleado,))
            result = cursor.fetchone()

        if result is not None:
            # La identificación existe, continuar con normalidad
            return True
        else:
            # La identificación no existe, mostrar alerta
            alerta = ft.AlertDialog(
                title=ft.Text("Identificación No Encontrada"),
                content=ft.Text("La identificación no existe"),
            )
            page.dialog = alerta
            alerta.open = True
            page.update()
            return False

    # Obtine la hora y fecha en el momento que seleccionan el boton de registro
    def obtener_fecha_hora_actual():
        now = datetime.now()
        fecha_actual = now.strftime("%d/%m/%Y")
        hora_actual = now.strftime("%I:%M %p")
        return fecha_actual, hora_actual
    
    # Crea una barra que contiene un titulo
    page.appbar = ft.AppBar(
        title=ft.Text("Registro Entrada"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    # Establecer conexión a la base de datos
    conexion = establecer_conexion()

    # logica al presionar el boton de registro
    def button_clicked(e):
        
        # Ejecuta la funcion que revisa la existencia del identificador
        if not Existencia_id(conexion):
            # La identificación no existe, no continuar con el proceso
            return
    
        fecha_actual, hora_entrada = obtener_fecha_hora_actual()

        # Resto del código para la inserción en la base de datos
        sql = "INSERT INTO registros (ID, fecha_entrada, Hora_entrada) VALUES (%s, %s, %s)"
        val = (Empleado.value, fecha_actual, hora_entrada)

        with conexion.cursor() as cursor:
            cursor.execute(sql, val)
            conexion.commit()
            print(cursor.rowcount, "record inserted.")
        
        dlg = ft.AlertDialog(
            title=ft.Text("    ¡Registro Exitoso!"),
            )
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Crear el campo para ingresar el identifiacador
    Empleado = ft.TextField(label="ID")
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

    # Agregar elementos a la página
    page.add(row_1, row_2)

# Iniciar la aplicación
ft.app(target=Entradas)
