import flet as ft
import os

def Main(page: ft.Page):
    page.title = "Mi app"
    page.appbar = ft.AppBar(
        title=ft.Text("Mi App"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )

    def open_file(file_name):
        # Cambia la ruta según la ubicación de tus archivos en la carpeta "usos"
        file_path = os.path.join("usos", file_name)
        os.system(f"python {file_path}")

    icon_1 = ft.IconButton(
        icon=ft.icons.APP_REGISTRATION_OUTLINED,
        on_click=lambda _: open_file("Inscripcion.py"),
        icon_color="blue400",
        icon_size=60,
        tooltip="Inscripcion",
    )

    icon_2 = ft.IconButton(
        icon=ft.icons.PERSON,
        on_click=lambda _: open_file("Registro_entrada.py"),
        icon_color="green",
        icon_size=60,
        tooltip="Registro entrada",
    )

    icon_3 = ft.IconButton(
        icon=ft.icons.PERSON,
        on_click=lambda _: open_file("Registro_entrada.py"),
        icon_color="blue",
        icon_size=60,
        tooltip="Registro salida",
    )

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

    page.add(row_1, ft.Divider(height=1, color="grai"),ft.VerticalDivider(width=1, color="white"),row_2)

ft.app(target=Main)
