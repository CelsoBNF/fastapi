from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'data': {'Celso': 'Natal'}}


@app.get('/player')
def player():
    return {'data': {'Player page'}}