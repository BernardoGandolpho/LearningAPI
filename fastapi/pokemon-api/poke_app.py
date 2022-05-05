from typing import List, Optional, Set

from fastapi import Body, FastAPI, Path, Query
from pydantic import BaseModel, Field

from db_pokemon import data


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
    types: Set[str] = []
    moveset: Optional[List[Move]] = None


# Database to be replaced
db_place_holder = data


# Routes
@app.get("/")
async def root():
    return {"message": "Salve"}


@app.get("/pokemons")
async def list_pokemon(
        skip: Optional[int] = Query(0),
        limit: Optional[int] = Query(10)):
    return db_place_holder[skip : skip + limit]


@app.get("/pokemons/{id}")
async def find_pokemon(
        id: int = Path(..., ge=0, lt=906)):
    return db_place_holder[id]


@app.get("/pokemons/{id}/moveset")
async def list_moveset(
        id: int = Path(..., ge=0, lt=906),
        skip: Optional[int] = Query(0),
        limit: Optional[int] = Query(10)):
    results = db_place_holder[id]["moveset"][skip : skip + limit]
    return results


@app.get("/pokemons/{id}/moveset/{move_id}")
async def find_move(
        id: int = Path(..., ge=0, lt=906),
        move_id: int = Path(..., ge=0, lt=2)):
    return db_place_holder[id]["moveset"][move_id]