from pydantic import BaseModel, Field


class User(BaseModel):
    order: int = Field(gt=0, description='Height of the pokemon')
    name: str = Field(description='name of the pokemon')
    height: float = Field(gt=0, description='Weight of the pokemon')# gt: for numeric values (int, float, Decimal), adds a validation of "greater than"
    weight: float = Field(gt=0, description='Height of the pokemon') #gt = "greater than"