from fastapi import FastAPI

from card.routers import authentication
from card import models
from card.database import engine
from card.routers import card, user
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(card.router)
app.include_router(user.router)
