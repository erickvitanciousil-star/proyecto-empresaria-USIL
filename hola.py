import flet as ft
from flet_fastapi import app as flet_fastapi_app

def main(page: ft.Page):
    page.title = "App Flet USIL"
    page.add(ft.Text("¡Hola! Tu aplicación en Flet ya está en línea correctamente.", size=20))

app = flet_fastapi_app(main, assets_dir="assets")

if __name__ == "__main__":
    ft.app(target=main)