import asyncio
import httpx
from API_training.poke_API.types_pydantic import User, PokeORM

async def get_pokemon(client, url):
        resp = await client.get(url) #AWAIT --> fazer todos os get e depois continuar
        pokemon = resp.json()
        pokes_pydantic = User(**{p:pokemon[p] for p in ["order", "name", "height", "weight"]})
        pokes = PokeORM(**dict(pokes_pydantic))
        return pokes

async def main():
    async with httpx.AsyncClient() as client:
        lista = []
        # lista_orm = []
        for number in range(1, 20):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            novo_poke = asyncio.ensure_future(get_pokemon(client, url))
            lista.append(novo_poke)

        return await asyncio.gather(*lista)

asyncio.run(main())
lst = list(asyncio.run(main()))
# print(lst)

