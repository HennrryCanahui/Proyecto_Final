import flet as ft
import os

# esto contendra todo el apartado grafico
def Main(page: ft.Page):
    page.title = "Mi app"
    # crea una barra con un titulo centrado
    page.appbar = ft.AppBar(
        title=ft.Text("Mi App"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    # Esta funcion abre los archivos en la carpeta usos  

    def open_file(file_name):
        # Cambia la ruta según la ubicación de los archivos 
        file_path = os.path.join("usos", file_name)
        os.system(f"python {file_path}")

    # Esto son botones en forma de iconos.
    icon_1 = ft.IconButton(
        icon=ft.icons.APP_REGISTRATION_OUTLINED,
        on_click=lambda _: open_file("Inscripcion.py"), # Tiene definido a que archivo es referenciado de lar carpeta usos
        icon_color="blue400",
        icon_size=60,
        tooltip="Inscripcion",
    )

    icon_2 = ft.IconButton(
        icon=ft.icons.PERSON,
        on_click=lambda _: open_file("Registro_entrada.py"),  # Tiene definido a que archivo es referenciado de lar carpeta usos
        icon_color="green",
        icon_size=60,
        tooltip="Registro entrada",
    )

    icon_3 = ft.IconButton(
        icon=ft.icons.PERSON,
        on_click=lambda _: open_file("Registro_salida.py"),  # Tiene definido a que archivo es referenciado de lar carpeta usos
        icon_color="blue",
        icon_size=60,
        tooltip="Registro salida",
    )

    # Esto guarda los iconos en contenedores para darle forma o orden 
    row_1 = ft.Row(controls=[
        ft.Container(expand=1),
        ft.Container(icon_1, expand=1),
        ft.Container(expand=1),
    ])

    row_2 = ft.Row(controls=[
        ft.Container(expand=1),
        ft.Container(icon_2, expand=1),
        
        ft.Container(icon_3, expand=1),
        ft.Container(expand=1),
    ])

    # Muestra el contenido con su logica
    page.add(row_1, ft.Divider(height=1, color="grai"),ft.VerticalDivider(width=1, color="white"),row_2)

# Inicia la aplicacion
ft.app(target=Main)
