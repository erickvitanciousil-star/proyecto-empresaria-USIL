import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Ruta absoluta a la carpeta dist generada por flet publish
dist_path = os.path.abspath("dist")

# Montar archivos estáticos (JS, assets, WASM)
app.mount("/static", StaticFiles(directory=dist_path), name="static")

@app.get("/{catchall:path}")
async def serve_app(catchall: str):
    file_path = os.path.join(dist_path, catchall)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse(os.path.join(dist_path, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hola:app", host="0.0.0.0", port=8000)