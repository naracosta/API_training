import asyncio
import httpx
import time

start_time = time.time()
lista = []
lista2 = {}
async def main():

    async with httpx.AsyncClient() as client:

        for number in range(1, 200):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}' #vai sempre mudar o valor do numero até o 151

            resp = await client.get(pokemon_url)
            pokemon = resp.json()
            #print([pokemon['order'], pokemon['name'], pokemon['height'], pokemon['weight']])
            lista.append([pokemon['order'], pokemon['name'], pokemon['height'], pokemon['weight']])
            # lista2.append('order': pokemon['order'])
            #print(pokemon['order'])

asyncio.run(main())
print(lista)
