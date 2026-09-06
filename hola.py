import flet as ft

def main(page: ft.Page):
    # Aquí va todo el código principal de tu interfaz
    page.title = "App Flet USIL"
    page.add(ft.Text("¡Hola! Tu aplicación en Flet ya está en línea correctamente.", size=20))

if __name__ == "__main__":
    ft.app(
        target=main, 
        assets_dir="assets",
        secret_key="mi_clave_secreta_flet"
    )