import flet as ft
import flet_fastapi

async def main(page: ft.Page):
    page.title = "Desayunos Express - USIL"
    page.add(ft.Text("¡Aplicación Desayunos Express en línea!", size=24, weight="bold"))

# Crear la app web de Flet compatible con uvicorn
app = flet_fastapi.app(main)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hola:app", host="0.0.0.0", port=8000)