import flet as ft
import flet_fastapi

def main(page: ft.Page):
    page.title = "App Flet USIL"
    page.add(ft.Text("¡Hola! Tu aplicación en Flet ya está en línea correctamente.", size=20))

# Crear la aplicación FastAPI asignada
app = flet_fastapi.app(main, assets_dir="assets")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")