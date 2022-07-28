#importamos por nivel de abstraccion desde modulos nativos de python,
#hasta modulos de terceros
#Python
from typing import Optional
#Pydantic

from pydantic import BaseModel
#FastAPI
from fastapi import FastAPI, Body, Query, Path

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


#Validation query parameter example
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="The name of the person, It's between 1 and 50 characters",
        ), 
     age: int = Query(
        ...,
        title='Person Age',
        description='This is the person name, is required',
        )
     ):

    return {"name": name, "age": age}

# validation path parameter example
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
            ...,
            gt=0,
            title="Person ID",
            description="The ID of the person, It's greater than 0"

            ) #el triple punto es para que sea obligatorio el parametro
    ):
    return {"person_id": person_id, person_id: "it exists"} 





