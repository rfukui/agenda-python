from app import app
from flask import request
from .services import get, get_all, cria_professor


@app.get('/test')
def test():
    return 'it works!'


@app.get('/professores/')
def _get_all():
    return get_all()

@app.post('/professores/')
def _create():
    return cria_professor(request.get_json())


@app.get('/professores/<int:_id>')
def _get(_id: int):
    return get(_id=_id)

