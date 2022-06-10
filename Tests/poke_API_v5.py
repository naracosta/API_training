from API_training.HTTPX.types_pydanic import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from API_training.HTTPX.types_pydanic import User, PokeORM
import httpx


for number in range(1, 3):
    lista = []
    pokezin = []
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}' #vai sempre mudar o valor do numero até o 151
    resp = httpx.get(pokemon_url)
    pokemon = resp.json()
    pokes_pydantic = User(**{p:pokemon[p] for p in ["order", "name", "height", "weight"]})
    poke = PokeORM(**dict(pokes_pydantic))
    poke = lista.append(poke)

print(lista)