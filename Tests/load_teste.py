from API_training.HTTPX.types_pydanic import Base
from API_training.HTTPX.poke_API_v4 import run
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///enterprise_TESTE.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

session.bulk_save_objects(run) #adiciona o dado no banco de dados
session.commit()