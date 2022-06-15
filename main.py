from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get('/')
def index():
    return {'data': {'blog list'}}


@app.get('/card')
def allcards():
    return {'data': {'Player page'}}


@app.get('/card/{name}')
def cardname(name: str):
    return {'data': name}


class Card(BaseModel):
    id: int
    name:str
    edition:str
    language:str
    foil:str
    price:float
    quantity:int


@app.post('/card')
def storecard(card: Card):
    return {'data': f"The card's stored with name as {card.name}"}
