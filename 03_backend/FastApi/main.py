from fastapi import FastAPI # Importamos FastApi
from routers import products, users # Importamos los modulos de rutas que hemos creado.
from fastapi.staticfiles import StaticFiles # Agregamos la clase para manejar archivos estáticos.

app = FastAPI() # Creamos la instancia de FastApi

# Agregamos los rutas a nuestra aplicación
app.include_router(products.router) # Agrego la ruta de products
app.include_router(users.router) # Agrego la ruta de users
app.mount("/static", StaticFiles(directory='static'), name = "static") # Monta el directorio /static en /static del servidor

@app.get("/") # Decorador para definir una ruta GET en /
async def root(): #  Es una función asincrona, por lo que se utiliza "async"
    return "Hola desde FastApi"  # Retornamos un mensaje a través del cuerpo de la respuesta HTTP

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"} #  Retornamos un json con el contenido que queremos mostrar

