import flet as ft
from flet_fastapi import app as flet_fastapi_app
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

def main(page: ft.Page):
    page.title = "Desayunos Express - USIL"
    page.add(ft.Text("¡Aplicación Desayunos Express en línea!", size=24, weight="bold"))

# Crear instancia principal de FastAPI
app = FastAPI()

# Montar la carpeta de assets si existe
if os.path.exists("assets"):
    app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Montar la aplicación de Flet en la raíz /
app.mount("/", flet_fastapi_app(main))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hola:app", host="0.0.0.0", port=8000, reload=True)