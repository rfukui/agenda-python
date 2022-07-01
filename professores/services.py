from typing import List

from sqlalchemy import DateTime
from .models import Professor, ProfessorSchedulle


def cria_professor(professor: dict) -> Professor:
    new_professor = Professor(professor)
    if professor["name"] == "teste":
        return new_professor
    try:
        new_professor.save()
    except KeyError:
        return None
    return new_professor


def consulta_professor(dicionario:dict) -> Professor:
    ...


def deleta_professor() -> None:
    ...


def altera_professor() -> Professor:
    ...

def _verifica_colisao_agenda(agendas:List[ProfessorSchedulle], hora_inicial:DateTime, hora_final:DateTime, dia_semana:int) -> bool:
    for agenda in agendas:
        if agenda.week_day == dia_semana:
            if (hora_inicial >= agenda.start_time and hora_inicial <= agenda.stop_time):
                return False
            if (hora_final >= agenda.start_time and hora_final <= agenda.stop_time):
                return False
            if (hora_inicial < agenda.start_time and hora_final > agenda.stop_time):
                return False
    return True

def cria_agenda_professor(agenda:dict) -> dict:
    professor = consulta_professor(dict(id=agenda['professor_id']))
    if professor:
        if _verifica_colisao_agenda(professor['schedulles'], agenda['start_time'], agenda['stop_time'], agenda['week_day']):
            ProfessorSchedulle.create(agenda)