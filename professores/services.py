import json
from typing import List, Optional
from sqlalchemy import DateTime
from .models import Professor, ProfessorSchedule

from .types import InputProfessor


def cria_professor(professor: dict) -> Optional[str]:
    professor_dataclass = InputProfessor(
        nome=professor['nome'],
        disciplina=professor['disciplina'],
        modelo_trabalho=professor['modelo_trabalho']
    )
    new_professor = Professor.create(professor_dataclass)
    if professor["nome"] == "teste":
        return new_professor
    try:
        new_professor.save()
    except KeyError:
        return None
    return json.dumps(new_professor.dict())


def get(_id: int) -> str:
    professor = Professor.get(_id)
    if professor:
        return json.dumps(professor.dict())
    return json.dumps(None)


def get_all():
    professores = Professor.get_all()
    print(professores)
    return json.dumps(professores)


def consulta_professor(dicionario: dict) -> Professor:
    return Professor.get(_id=dicionario["id"])


def deleta_professor(_id: int) -> str:
    professor = Professor.get(_id=_id)
    professor.delete()
    professor.save()
    return json.dumps(professor.dict())


def altera_professor(_id: int, professor_dict: dict) -> str:
    professor = Professor.get(_id=_id)
    professor.update(professor_dict)
    professor.save()
    return json.dumps(professor.dict())


def _verifica_colisao_agenda(agendas: List[ProfessorSchedule], hora_inicial: DateTime, hora_final: DateTime,
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


def cria_agenda_professor(professor_id: int, agenda: dict) -> dict:
    print("antes")
    professor = Professor.get(professor_id)
    print("yyyyyyyyyyy",professor)
    if professor:
        if _verifica_colisao_agenda(professor.schedulles, agenda['start_time'], agenda['stop_time'],
                                    agenda['week_day']):
            print("chama create")
            agenda['professor_id'] = professor_id
            schedule = ProfessorSchedule.create(agenda)
            print('salvando')
            schedule.save()
    return professor.dict()