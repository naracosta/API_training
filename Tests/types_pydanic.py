from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PokeORM(Base):
    __tablename__ = 'pokemon' #nome da tabela do banco
    order = Column(Integer, primary_key=True, autoincrement=True) #tipo column e tipo inteiro
    name = Column(String(255), nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)

    def __repr__(self):
        return f'Pokemon({self.name})'

class User(BaseModel):
    order: int = Field(gt=0, description='Number of the pokemon')
    name: str = Field(description='Name of the pokemon')
    height: float = Field(gt=0, description='Weight of the pokemon')# gt: for numeric values (int, float, Decimal), adds a validation of "greater than"
    weight: float = Field(gt=0, description='Height of the pokemon') #gt = "greater than"

    class Config:
        orm_mode = True