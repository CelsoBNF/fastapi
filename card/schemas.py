from typing import List, Optional
from pydantic import BaseModel


class CardBase(BaseModel):
    name:str
    edition:str
    language:str
    foil:str
    price:float
    quantity:float

class Card(CardBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name:str
    email:str
    password:str


class ShowUser(BaseModel):
    name:str
    email:str
    cards: List[Card] = []
    class Config():
        orm_mode = True

class ShowCard(BaseModel):
    player: ShowUser
    name:str
    edition:str
    language:str
    foil:str
    price:float
    quantity:float

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
