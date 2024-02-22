from fastapi import FastAPI # Importamos FastApi
from pydantic import BaseModel # Importamos la clase base de PyDantic para crear nuestra propia clase.

app = FastAPI() # Creamos la instancia de FastApi

### ENTIDAD USER ###
class User(BaseModel): # Creación de la clase "User" heredando de BaseModel, que implementa las validaciones
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



# METODO GET PATH  recomendado para parametros fijos
@app.get('/users/')
async def users():
    return users_list

# METODO GET PATH  recomendado para parametros fijos
@app.get('/user/{id}')
async def user(id: int):
    return search_user(id)


# METODO GET QUERY recomendado para parametros dinamicos
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)


# METODO POST CREAR USUARIO
@app.post('/user/') #  Ruta POST en /user/
async def user(user: User): #  El nombre del parámetro debe ser igual al nombre de la clase
        if type(search_user(user.id)) == User: # Compruebo si el usuario existe antes de crearlo
            return {"Error al crear el usuario": "El usuario ya existe"} # Devuelve un error si el usuario existe
        else:            
            users_list.append(user) # Si el usuario no existe lo crea correctamente
            return user
        
        
# METODO PUT MODIFICAR USUARIO
@app.put('/user/')  # Ruta PUT en /user/
async def user(user: User):   # Recibe un objeto User con los datos a modificar
    found = False   # Bandera para saber si se ha encontrado al usuario
    for index, saved_user in enumerate(users_list):  # Recorrido de la lista de usuarios
        if saved_user.id == user.id:   # Pregunto si existe el usuario
            users_list[index] = user   # Modifico los datos del usuario existente con los nuevos
            found = True    # Marco como encontrado y salgo del bucle            
    if not  found:   # Si no ha encontrado el usuario (es nuevo)
        return {"error": "Usuario no actualizado"}
    else:         # Devuelvo el mensaje de confirmación de modificación
        return user

# METODO DEL ELIMINAR USUARIO
@app.delete('/user/{id}')   # Ruta DELETE en /user/
async def user(id: int):    # No recibe parámetros, se utiliza para eliminar todos los usuarios
    found = False   # Bandera para saber si se ha encontrado al usuario    
    for index, saved_user in enumerate(users_list):  # Recorrido de la lista de usuarios
        if saved_user.id == id:   # Pregunto si existe el usuario
            del users_list[index] # Modifico los datos del usuario existente con los nuevos
            found = True    # Marco como encontrado y salgo del bucle  
    if not  found:   # Si no ha encontrado el usuario (es nuevo)
        return {"error": "No se ha eliminado el usuario"}
    else:         # Devuelvo el mensaje de confirmación de modificación
        return {"Usuario eliminado correctamente"}       
            
        


#### DEFINICION DE CLASES ####
##############################

#### CLASE BUSCA USUARIO
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
