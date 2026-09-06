import os
import flet as ft
import flet_fastapi

# Obtener la ruta absoluta de la carpeta assets
assets_dir = os.path.abspath("assets")

def main(page: ft.Page):
    page.title = "Desayunos Express - USIL"
    page.add(ft.Text("¡Aplicación Desayunos Express en línea!", size=24, weight="bold"))

# Se pasa la ruta absoluta a flet_fastapi
app = flet_fastapi.app(main, assets_dir=assets_dir)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hola:app", host="0.0.0.0", port=8000)