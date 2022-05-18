from types_pydanic import User
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
            print(**pokemon['name'])

asyncio.run(main())
# print("--- %s seconds ---" % (time.time() - start_time))


from types_pydanic import User

external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}
user = User(**external_data)
print(user.id)

print(repr(user.signup_ts))

#print(user.friends)

print(user.dict())

