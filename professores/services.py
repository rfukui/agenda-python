import json
from typing import List, Optional

from sqlalchemy import DateTime
from .models import Professor, ProfessorSchedulle

from .types import InputProfessor

def cria_professor(professor: dict) -> Optional[Professor]:
    professor_dataclass = InputProfessor(nome=professor['nome'], disciplina=professor['disciplina'], modelo_trabalho=professor['modelo_trabalho'])
    new_professor = Professor.create(professor_dataclass)
    if professor["nome"] == "teste":
        return new_professor
    try:
        new_professor.save()
    except KeyError:
        return None
    return new_professor


def get(_id: int) -> dict:
    """

    :rtype: object
    """
    return json.dumps(Professor.get(_id))
def get_all():
    return json.dumps(Professor.get_all())


def consulta_professor(dicionario: dict) -> Professor:
    return Professor.get(id=dicionario["id"])


def deleta_professor(dicionario: dict) -> Professor:
    return Professor.delete(id=dicionario["id"])


def altera_professor(dicionario: dict) -> Professor:
    professor = Professor.get(id=dicionario[id])
    professor.update(dicionario)


def _verifica_colisao_agenda(agendas: List[ProfessorSchedulle], hora_inicial: DateTime, hora_final: DateTime,
                             dia_semana: int) -> bool:
    for agenda in agendas:
        if agenda.week_day == dia_semana:
            if agenda.start_time <= hora_inicial <= agenda.stop_time:
                return False
            if agenda.start_time <= hora_final <= agenda.stop_time:
                return False
            if hora_inicial < agenda.start_time and hora_final > agenda.stop_time:
                return False
    return True


def cria_agenda_professor(agenda: dict) -> dict:
    professor = consulta_professor(dict(id=agenda['professor_id']))
    if professor:
        if _verifica_colisao_agenda(professor['schedulles'], agenda['start_time'], agenda['stop_time'],
                                    agenda['week_day']):
            ProfessorSchedulle.create(agenda)
