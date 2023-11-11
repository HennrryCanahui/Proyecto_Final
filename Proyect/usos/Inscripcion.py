import mysql.connector
import flet as ft
import random

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

# Función para generar un número único
def generar_numero_unico(conexion):
    while True:
        numero_generado = random.randint(1000, 9999)
        if not verificar_numero(numero_generado, conexion):
            return numero_generado

# Función para verificar si el número ya existe en la base de datos
def verificar_numero(numero, conexion):
    query = "SELECT * FROM empleados WHERE Identificación = %s"
    with conexion.cursor() as cursor:
        cursor.execute(query, (numero,))
        return cursor.fetchone() is not None

# Función principal para el formulario
def Registro(page: ft.Page):

    # Crea una barra que contiene un titulo
    page.appbar = ft.AppBar(
        title=ft.Text("Registro"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    # establece la conececcion y la almacena en una variable
    conexion = establecer_conexion()

    # tb1 es el numero generado
    tb1 = None  

    # Revisa que los campos del formulario no esten vacios 
    def validar_campos_vacios():
        campos = [tb2, tb3, tb4, tb5, tb6_1, tb6_2, tb6_3, tb7, tb7_1, tb8, tb8_1, tb9]  # Lista de campos a verificar
        campos_vacios = []
        for campo in campos:
            if isinstance(campo, ft.Dropdown):  # Verificar si el campo es un Dropdown
                if campo.value is None:
                    campos_vacios.append(str(campo.label))
            elif campo.value.strip() == "":
                campos_vacios.append(str(campo.label))

        if campos_vacios:
        # Mostrar alerta si hay campos vacíos
            alerta = ft.AlertDialog(
                title=ft.Text("Campos Vacíos"),
                content=ft.Text(f"Los siguientes campos están vacíos: {', '.join(campos_vacios)}"),
            )
            page.dialog = alerta
            alerta.open = True
            page.update()
            return False
        else:
            return True

    # Función ejecutada al hacer clic en el botón
    def button_clicked(e):

        # Revisa si hay campos de informacion vacios y si hay manda un mensaje
        if not validar_campos_vacios():
            return # si no encuentra nada sigue el programa con normalida

        nonlocal tb1  # Hacer referencia a la variable externa tb1
        tb1 = generar_numero_unico(conexion)  # Generar un nuevo número único
        print(tb1)
        
        # Unificar los datos de la fechas
        fecha_Comienso = f"{tb6_1.value}/{tb6_2.value}/{tb6_3.value}"
        
        # Unificar tb7 y tb7_1
        hora_entrada = f"{tb7.value} {tb7_1.value}"  # Concatenar los valores

        # Unificar tb8 y tb8_1
        hora_salida = f"{tb8.value} {tb8_1.value}"  # Concatenar los valores

        # Preparar y ejecutar la consulta SQL para insertar datos en la base de datos
        sql = "INSERT INTO empleados(Identificación, Nombre, Apellidos, Edad, Recidencia, Fecha_Inicio, Hora_Entrada, Hora_Salida, Sueldo) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"
        val = (tb1, tb2.value, tb3.value, tb4.value, tb5.value, fecha_Comienso, hora_entrada, hora_salida, tb9.value)

        # Ejecuta el insert con los datos del formulario
        with conexion.cursor() as cursor:
            cursor.execute(sql, val)

            conexion.commit()
        

            print(cursor.rowcount, "record inserted.")
            #limpia las entradas de texto
            tb2.value = ""
            tb3.value = ""
            tb4.value = ""
            tb5.value = ""
            tb6_1.value = ""
            tb6_2.value = ""
            tb6_3.value = ""
            tb7.value = ""
            tb7_1.value = ""
            tb8.value = ""
            tb8_1.value = ""
            tb9.value = ""
        page.update()

        # Muestra el identifacador del empleado
        dlg = ft.AlertDialog(
            title=ft.Text("¡Registro Exitoso!"),
            content=ft.Text(f"El identificador es : {tb1}"),
            )
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Definir campos de texto y botón
    tb2 = ft.TextField(label="Nombres",)
    tb3 = ft.TextField(label="Apellidos")
    tb4 = ft.TextField(label="Edad")
    tb5 = ft.TextField(label="Recidencia")
    tb6_1 = ft.TextField(label="Dia_Inicio")
    tb6_2 = ft.TextField(label="Mes_Inicio")
    tb6_3 = ft.TextField(label="Año_Inicio")


    tb7 = ft.TextField(label="Hora_Entrada")
    tb7_1 = ft.Dropdown(
        label="A.M , P.M",
        width=100,
        options=[
            ft.dropdown.Option("A.M", ),
            ft.dropdown.Option("P.M"),
            
        ],
    )
    
    tb8 = ft.TextField(label="Hora_Salida")
    tb8_1 = ft.Dropdown(
        label="A.M , P.M",
        width=100,
        options=[
            ft.dropdown.Option("A.M"),
            ft.dropdown.Option("P.M"),
        ],
    )

    tb9 = ft.TextField(label="Sueldo")
    b = ft.ElevatedButton(text="Registrar", on_click=button_clicked)

    # Añadir campos y botón a la página
    page.add(
        ft.Row(controls=[ft.Container(
                            tb2,
                            expand=1,
                        ),
                        ft.Container(
                            tb3,
                            expand=1,
                        ),
                            ]),

        tb4, tb5, 
        ft.Row(controls=[ft.Container(
                            tb6_1,
                            expand=1,
                        ),
                        ft.Container(
                            tb6_2,
                            expand=1,
                        ),
                        ft.Container(
                            tb6_3,
                            expand=1,
                        ),
                            ]),

        ft.Row(controls=[ft.Container(
                            tb7,
                            expand=3,
                        ),
                        ft.Container(
                            tb7_1,
                            expand=1,
                        ),
                            
                        ft.Container(
                            tb8,
                            expand=3,
                        ),
                        ft.Container(
                            tb8_1,
                            expand=1,
                        ),
                            ]),
        tb9,

        ft.Row(controls=[ft.Container(
                            b,
                            expand= 1
                        ),
                        ft.Container(
                            
                            expand= 2
                        )]
                )
            )
                            
# Iniciar la aplicación
ft.app(Registro)