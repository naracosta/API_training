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
    # pokes_orm = lista.append([PokeORM(
    #             order=p.order,
    #             name=p.name,
    #             height=p.height,
    #             weight=p.weight,
    #         ) for p in pokes_pydantic])
    poke = lista.append(poke)

print(lista)

# banco =  sqlite3.connect('first_database.db') #criando o seu banco de dados com o nome: 'first_database.db'

engine = create_engine('sqlite:///enterprise_TESTE.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
session.add_all(lista) #adiciona o dado no banco de dados
session.commit()