from sqlalchemy import Column, Float, ForeignKey, String, Integer
from card.database import Base
from sqlalchemy.orm import relationship


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    edition = Column(String)
    language = Column(String)
    foil = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    player = relationship("User", back_populates="cards")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    cards = relationship('Card', back_populates="player")
