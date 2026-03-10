from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class pokemon (BaseModel):
    id:  int
    name: str
    attack : int
    life : int
    type : str

pokemons =[
    pokemon(id = 1, name ="miguel", attack=45, life= 100, type= "fuego"), 
    pokemon(id = 2, name ="jorge", attack=76, life= 100, type= "agua"), 
    pokemon(id = 3, name ="maritza", attack=21, life= 100, type= "aire"), 
    pokemon(id = 4, name ="jorgeeduardo", attack=67, life= 100, type= "libre"), 
    pokemon(id = 5, name ="sebas", attack=12, life= 100, type= "serio"), 
    pokemon(id = 5, name ="amelia", attack=99, life= 100, type= "felicidad"), 
    
    ]

@app.get("/mostrartodos")
def mostrar_todos():
    return pokemons

@app.get("/mostraruna")
def mostrar_nombre(nombre:str):
    for pokemon in pokemons:
        if pokemon.name == nombre:
            return pokemon
        
    return {"mensaje":"pokemon no encontrado"}

@app.get("/mostrarid")
def mostrar_id(id:int):
    for pokemon in pokemons:
        if pokemon.id == id:
            return pokemon
    return {
        "mensaje":"pokemon no encontrado por id"
    }