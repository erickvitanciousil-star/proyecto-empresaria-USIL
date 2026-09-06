import flet as ft
import flet_fastapi

def main(page: ft.Page):
    page.title = "Desayunos Express - USIL"
    page.add(ft.Text("¡Aplicación Desayunos Express en línea!", size=24, weight="bold"))

# flet_fastapi requiere una función síncrona como target
app = flet_fastapi.app(main)