from app import app
from flask import request
from .services import get, get_all, cria_professor, altera_professor, deleta_professor, cria_agenda_professor


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



@app.post('/professores/<int:professor_id>/agenda/')
def create_schedulle(professor_id: int):
    print("xxxxxxxxxxxx", professor_id)

    return cria_agenda_professor(professor_id, request.get_json())


# @app.get('/professores/<int:professor_id>/agenda/')
# def _get_agenda_professor(professor_id: int):
#     return get(_id=_id)
#
#
# @app.put('/professores/<int:professor_id>/agenda/<int:agenda_id>')
# def _altera_professor(professor_id: int, agenda_id: int):
#     return altera_professor(_id=_id,professor_dict=request.get_json())


