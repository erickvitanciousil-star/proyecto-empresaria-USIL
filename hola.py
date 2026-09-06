import flet as ft
import flet_fastapi

def main(page: ft.Page):
    # Tu código actual de la app
    page.add(ft.Text("¡App Flet cargada con éxito!"))

# Monta la aplicación con soporte para assets/imágenes
app = flet_fastapi.app(main, assets_dir="assets")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")