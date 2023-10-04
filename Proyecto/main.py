
from Usos.Conector import *
import flet as ft

Entrada = conexion.cursor()

def main(page: ft.Page):
    def button_clicked(e):

        sql = "INSERT INTO pruebas_1(Identificacion, Nombres, Apellidos, Edad, Recidencia, Fecha_Inicio, Hora_Entrada, Hora_Salida, Sueldo) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s)"
        val = (tb1.value, tb2.value, tb3.value, tb4.value, tb5.value, tb6.value, tb7.value, tb8.value, tb9.value)
        Entrada.execute(sql, val)
        conexion.commit()
        print(Entrada.rowcount, "record inserted.")
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="ola")
    tb2 = ft.TextField(label="Nombres")
    tb3 = ft.TextField(label="Apellidos")
    tb4 = ft.TextField(label="Edad")
    tb5 = ft.TextField(label="Recidencia")
    tb6 = ft.TextField(label="Fecha_Inicio")
    tb7 = ft.TextField(label="Hora_Entrada")
    tb8 = ft.TextField(label="Hora_Salida")
    tb9 = ft.TextField(label="Sueldo")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9,b, t)

ft.app(main)