#importamos por nivel de abstraccion desde modulos nativos de python,
#hasta modulos de terceros
#Python
from typing import Optional
#Pydantic

from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI, Body

#Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    #optional attributes
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None
    


app = FastAPI()


#basic path operation example
@app.get("/")
def home():
    return {"message": "Hello World"}


#Request Body example
#tipado estatico
#el triple punto de body es para que sea obligatorio el parametro
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person








