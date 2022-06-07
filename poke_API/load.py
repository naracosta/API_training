from hashlib import new
from API_training.poke_API.types_pydantic import Base
from API_training.poke_API.extract import lst
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# banco =  sqlite3.connect('first_database.db') #criando o seu banco de dados com o nome: 'first_database.db'

engine = create_engine('sqlite:///enterprise.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
# session.bulk_save_objects(lst)
session.add_all(lst) #adiciona o dado no banco de dados
session.commit() #commita o dado no banco de dados