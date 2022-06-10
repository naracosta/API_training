#list_comprehension
import asyncio
from API_training.HTTPX.types_pydanic import User, PokeORM
import httpx
import time

lista = []
for number in range(1, 3):
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}' #vai sempre mudar o valor do numero até o 151
    resp = httpx.get(pokemon_url)
    pokemon = resp.json()
    pokes_orm = PokeORM(**{p:pokemon[p] for p in ["order", "name", "height", "weight"]})
    pokes = User.from_orm(pokes_orm)
    lista.append(pokes)

print(lista)

