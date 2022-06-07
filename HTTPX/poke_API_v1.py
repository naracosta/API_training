import asyncio
from API_training.HTTPX.types_pydanic import User
import httpx
import time


lista = []
for number in range(1, 3):
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}' #vai sempre mudar o valor do numero até o 151
    resp = httpx.get(pokemon_url)
    pokemon = resp.json()
    pokezinho = [pokemon['order'], pokemon['name'], pokemon['height'], pokemon['weight']]
    data = ["order", "name", "height", "weight"]
    dicionary = dict(zip(data, pokezinho)) # cria um dicionario
    new = User(**dicionary) #desempacota o que está dentro do dicionario (**)
    lista.append(new)

print(lista)

#list comprehension transforma linha 12-16 em 1 linha










