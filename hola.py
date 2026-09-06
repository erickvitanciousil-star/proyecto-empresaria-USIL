import flet as ft
from flet_fastapi import app as flet_fastapi_app

def main(page: ft.Page):
    # Tu código actual de la aplicación va aquí adentro
    pass

# Esta línea permite que Render/uvicorn ejecuten la app en la nube
app = flet_fastapi_app(main)

if __name__ == "__main__":
    ft.app(target=main)