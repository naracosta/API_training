import asyncio
import httpx
import time

lista = []
async def main():

    async with httpx.AsyncClient() as client:

        for number in range(1, 200):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}' #vai sempre mudar o valor do numero até o 151

            resp = await client.get(pokemon_url)
            pokemon = resp.json()
            lista.append([pokemon['order'], pokemon['name'], pokemon['height'], pokemon['weight']])

asyncio.run(main())
print(lista)
