from app import app
from flask import request
from .services import get, get_all, cria_professor, altera_professor, deleta_professor


@app.get('/professores/')
def _get_all():
    return get_all()


@app.post('/professores/')
def create():
    return cria_professor(request.get_json())


@app.get('/professores/<int:_id>')
def _get(_id: int):
    return get(_id=_id)


@app.put('/professores/<int:_id>')
def _altera_professor(_id):
    return altera_professor(_id=_id,professor_dict=request.get_json())


@app.delete('/professores/<int:_id>')
def _deleta_professor(_id):
    return deleta_professor(_id=_id)
