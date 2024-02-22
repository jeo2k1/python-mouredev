from fastapi import FastAPI # Importamos FastApi
from routers import products, users

app = FastAPI() # Creamos la instancia de FastApi

# Agregamos los rutas a nuestra aplicación
app.include_router(products.router)

@app.get("/") # Decorador para definir una ruta GET en /
async def root(): #  Es una función asincrona, por lo que se utiliza "async"
    return "Hola desde FastApi"  # Retornamos un mensaje a través del cuerpo de la respuesta HTTP

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"} #  Retornamos un json con el contenido que queremos mostrar

