from fastapi import FastAPI
from pydantic import BaseModel, Field

# Criando a aplicação com FastAPI
app = FastAPI()

# Função para encontrar o próximo id para requisições com método POST
def _find_next_id():
    return max(country.country_id for country in countries) + 1


# Modelo para cerificação e armazenamento dos registros
class Country(BaseModel):
    country_id: int = Field(default_factory=_find_next_id, alias="id")
    name: str
    capital: str
    area: int

# Lista de dicionários para simular um banco de dados
countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]


# Rotas
@app.get("/countries")
async def get_countries():
    return countries


@app.post("/countries", status_code=201)
async def add_country(country: Country):
    countries.append(country)
    return country