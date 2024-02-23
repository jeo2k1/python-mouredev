from fastapi import FastAPI # Importamos FastApi
from routers import products, users # Importamos los modulos de rutas que hemos creado.

app = FastAPI() # Creamos la instancia de FastApi

# Agregamos los rutas a nuestra aplicación
app.include_router(products.router) # Agrego la ruta de products
app.include_router(users.router) # Agrego la ruta de users


@app.get("/") # Decorador para definir una ruta GET en /
async def root(): #  Es una función asincrona, por lo que se utiliza "async"
    return "Hola desde FastApi"  # Retornamos un mensaje a través del cuerpo de la respuesta HTTP

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"} #  Retornamos un json con el contenido que queremos mostrar

