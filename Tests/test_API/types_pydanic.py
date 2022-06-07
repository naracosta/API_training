from pydantic import BaseModel

class User(BaseModel):
    order: int
    name: str
    height: int
    weight: int
