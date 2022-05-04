from fastapi import FastAPI
from pydantic import BaseModel, Field

# Creating FastAPI app
app = FastAPI()

# Funtion to find the next id for POST requests
def _find_next_id():
    return max(country.country_id for country in countries) + 1


# Model for validation and storage of registers
class Country(BaseModel):
    country_id: int = Field(default_factory=_find_next_id, alias="id")
    name: str
    capital: str
    area: int

# List of dictionaries to replace a database
countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]


# Routes
@app.get("/countries")
async def get_countries():
    return countries


@app.post("/countries", status_code=201)
async def add_country(country: Country):
    countries.append(country)
    return country