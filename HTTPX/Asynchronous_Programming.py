## Fazendo uma solicitação HTTP com HTTPX:
import asyncio
import httpx

async def main():
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon-species/aegislash'

    async with httpx.AsyncClient() as client:
        resp = await client.get(pokemon_url)
        pokemon = resp.json()
        print(pokemon['name'])

asyncio.run(main())

## ========================================================================
## Fazendo um grande número de solicitações:
import asyncio
import httpx
import time

start_time = time.time()

async def main():

    async with httpx.AsyncClient() as client:

        for number in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}' #vai sempre mudar o valor do numero até o 151

            resp = await client.get(pokemon_url)
            pokemon = resp.json()
            print(pokemon['name'])

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time)) #vai mostrar o tempo para o programa rodar

## ========================================================================
## Utilizando o assíncrono para melhorar o desempenho

import asyncio
import httpx
import time

start_time = time.time()

async def get_pokemon(client, url):
        resp = await client.get(url)
        pokemon = resp.json()
        return pokemon['name']

async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        lista_pokemon = []

        for number in range(1, 20):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.ensure_future(get_pokemon(client, url)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
