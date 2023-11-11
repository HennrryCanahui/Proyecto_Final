import flet as ft
import mysql.connector
from datetime import datetime

# Función para establecer una conexión a la base de datos MySQL.
def establecer_conexion():
    try:
        # Establecer la conexión a la base de datos MySQL
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

# Esta función obtiene la fecha actual en el formato "dd/mm/yyyy"
def obtener_fecha_actual():
    now = datetime.now()
    fecha_actual = now.strftime("%d/%m/%Y")
    return fecha_actual

# Esta función obtiene la hora actual en el formato "hh:mm AM/PM"
def obtener_hora_actual():
    now = datetime.now()
    hora_actual = now.strftime("%I:%M %p")
    return hora_actual

# Contiene el apartado gráfico
def Entradas(page: ft.Page):

    # Establecer conexión a la base de datos
    conexion = establecer_conexion()

    # Crea una barra que contiene un título
    page.appbar = ft.AppBar(
        title=ft.Text("Registro Salida"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    # Función para encontrar el No. del registro que cumple ciertas condiciones
    def encontrar_no(conexion):
        id_empleado = Empleado.value
        fecha_entrada = obtener_fecha_actual()
        query_verificacion =  "SELECT * FROM registros WHERE ID = %s AND fecha_entrada = %s AND Hora_Salida = ''"
        
        cursor = conexion.cursor()
        cursor.execute(query_verificacion, (id_empleado, fecha_entrada))
        result = cursor.fetchone()
        cursor.close()

        if result:
            return result[0]  # Devuelve el valor de la columna "No."
        else:
            return None  # No se encontró un registro válido

    # Función para actualizar la hora de salida en el registro encontrado
    def actualizar_hora_salida(conexion, no_registro):
        cursor = conexion.cursor()

        # Actualizar la columna "Hora_Salida" para el registro encontrado
        query_actualizacion = "UPDATE registros SET Hora_Salida = %s WHERE `No.` = %s"
        hora_salida_nueva = obtener_hora_actual()
        cursor.execute(query_actualizacion, (hora_salida_nueva, no_registro))

        # Confirmar la transacción
        conexion.commit()

        # Cerrar el cursor
        cursor.close()

    # Función que se ejecuta al hacer clic en el botón "Registrar"
    def button_clicked(e):
        # Encontrar el No. del registro que cumple las condiciones
        no_registro_encontrado = encontrar_no(conexion)

        if no_registro_encontrado is not None:
            actualizar_hora_salida(conexion, no_registro_encontrado)
            dlg = ft.AlertDialog(
            title=ft.Text("    ¡Registro Exitoso!"),
            )
            page.dialog = dlg
            dlg.open = True
            Empleado.value = ""
            page.update()
        else:
            dlg = ft.AlertDialog(
            title=ft.Text("No se encontró un registro válido"),
            )
            page.dialog = dlg
            dlg.open = True
            Empleado.value = ""
            page.update()

    # Crear elementos de la interfaz de usuario
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

# Ejecutar la aplicación
ft.app(target=Entradas)
