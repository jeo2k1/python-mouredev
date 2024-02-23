from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # Creamos la instancia de FastApi

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
users_db = {
    "jeo": {
        "username": "jeo",
        "full_name": "Jorge Orellana",
        "email": "jeo@jeo.com",
        "disabled": False,
        "password": "123456"
    },
    "jeo2": {
        "username": "jeo2",
        "full_name": "Jorge Orellana 2",
        "email": "jeo2@jeo2.com",
        "disabled": True,
        "password": "987654"
    }
}
