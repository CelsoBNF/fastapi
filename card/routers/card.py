from typing import List
from fastapi import APIRouter, Depends, status


from card import schemas, database, oauth2
from sqlalchemy.orm import Session
from card.repository import card


router = APIRouter(
    prefix = "/card",
    tags=['Cards']
)


get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowCard])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return card.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def storeCard(request: schemas.Card, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return card.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return card.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Card, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return card.update(id, request, db)


@router.get('/{name}', status_code=200, response_model=schemas.ShowCard)
def show(name, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return card.show(name, db)
