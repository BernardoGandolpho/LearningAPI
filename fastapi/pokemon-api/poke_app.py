from typing import List, Optional
import json

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field


app = FastAPI()


# Classes and Models
class Move(BaseModel):
    name: Optional[str] = Field(None, max_length=30)
    power: int = Field(..., ge=0)
    accuracy: Optional[float] = Field(1, gt=0, le=1)
    description: Optional[str] = Field(None, max_length=300)


class Pokemon(BaseModel):
    name: str = Field(..., min_length=3, max_length=30)
    pokedex_id: int = Field(..., gt=0, le=905)
    types: List[str] = []
    moveset: Optional[List[Move]] = None


# Database to be replaced
db_place_holder = None

with open("db_pokemon.json", "r") as file:
    db_place_holder = json.loads(file.read())


# Routes
@app.get("/")
async def root():
    return {"message": "Salve"}


@app.get("/pokemons")
async def list_pokemon(
        skip: Optional[int] = Query(0),
        limit: Optional[int] = Query(10)):
    return {"pokemons": db_place_holder[skip : skip + limit]}


@app.get("/pokemons/{id}")
async def find_pokemon(
        id: int = Path(..., ge=0, lt=906)):
    return {"Pokemon": db_place_holder[id]}


@app.get("/pokemons/{id}/moveset")
async def list_moveset(
        id: int = Path(..., ge=0, lt=906),
        skip: Optional[int] = Query(0),
        limit: Optional[int] = Query(10)):
    results = db_place_holder[id]["moveset"][skip : skip + limit]
    return {"moveset": results}


@app.get("/pokemons/{id}/moveset/{move_id}")
async def find_move(
        id: int = Path(..., ge=0, lt=906),
        move_id: int = Path(..., ge=0, lt=2)):
    return {"move": db_place_holder[id]["moveset"][move_id]}


@app.post("/pokemons", status_code=201)
async def create_pokemon(pokemon: Pokemon):
    new_pokemon = pokemon.dict()

    for pokemon in db_place_holder:
        if pokemon["pokedex_id"] == new_pokemon["pokedex_id"]:
            raise HTTPException(status_code=400, detail="Duplicate pokemon")

    db_place_holder.append(new_pokemon)

    db_place_holder.sort(key=lambda x: x["pokedex_id"])
    
    with open("db_pokemon.json", "w") as file:
        file.write(str(db_place_holder).replace("'", '"').replace(' None', ' "None"'))
    
    return (new_pokemon)