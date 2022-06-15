from sqlalchemy.orm import Session
from sqlalchemy import desc
from card import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    cards = db.query(models.Card).order_by(models.Card.price.desc()).all()
    return cards


def create(request: schemas.Card, db: Session):
    new_card = models.Card(name=request.name,
    edition=request.edition,
    language=request.language,
    foil=request.foil,
    price=request.price,
    user_id=1,
    quantity=request.quantity)
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card


def destroy(id:int, db: Session):
    card = db.query(models.Card).filter(models.Card.id == id)

    if not card.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"Card with id {id} not found")
    card.delete(synchronize_session=False)                              
    db.commit()
    return "done"


def update(id:int, request: schemas.Card, db:Session):
    card = db.query(models.Card).filter(models.Card.id == id )

    if not card.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail = f"Card with id {id} not found")

    card.update(request)
    db.commit()
    return 'updated'


def show(name:str, db:Session):
    card = db.query(models.Card).filter(models.Card.name == name).first()

    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Card with the name {name} is not available" )  
    return card
