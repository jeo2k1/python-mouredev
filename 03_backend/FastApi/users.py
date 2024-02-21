from fastapi import FastAPI # Importamos FastApi
from pydantic import BaseModel # Importamos la clase base de PyDantic para crear nuestra propia clase.

#### DEFINICION DE CLASES
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


###### FIN DEFINICION DE CLASES


app = FastAPI() # Creamos la instancia de FastApi

class User(BaseModel): #  Creación de la clase "User" heredando de BaseModel, es decir, que implementa las validaciones y serializaciones automáticas de PyDantic.
    id: int
    name: str
    surname: str
    url: str
    age: int
    
users_list = [User(id=1, name="JeO", surname="Orellana", url="https://www.infobae.com/", age=45),
              User(id=2, name="Pedro", surname="Orellana", url="https://www.ole.com.ar/", age=40),
              User(id=3, name="Juan", surname="Orellana", url="https://www.tiemposur.com.ar/", age=35)]


@app.get("/usersjson") # Decorador para definir una ruta GET en /usersjson
async def usersjson(): #  Es una función asincrona, por lo que se utiliza "async"
    return [{"name": "JeO", "surname": "Orellana", "url": "https://www.infobae.com/", "age": 45},
            {"name": "Pedro", "surname": "Orellana", "url": "https://www.ole.com.ar/", "age": 40},
            {"name": "Juan", "surname": "Orellana", "url": "https://www.tiemposur.com.ar/", "age": 35}]


# PATH
@app.get('/user/{id}')
async def user(id: int):
    return search_user(id)

# QUERY
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

