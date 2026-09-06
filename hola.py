import os
import flet as ft
import flet_fastapi

# Obtener ruta absoluta de la carpeta assets
assets_path = os.path.abspath("assets")

def main(page: ft.Page):
    # AQUÍ VA TODO EL CÓDIGO DE TU APP DESAYUNOS EXPRESS
    pass

# Inicialización estándar para servidores en producción
app = flet_fastapi.app(
    main, 
    assets_dir=assets_path,
    secret_key="desayunos_express_usil_secret_key"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hola:app", host="0.0.0.0", port=8000)