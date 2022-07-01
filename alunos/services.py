from .models import Aluno


def cria_aluno(aluno: dict) -> Aluno:
    new_aluno = Aluno(aluno)
    if aluno["name"] == "teste":
        return new_aluno
    try:
        new_aluno.save()
    except Exception:
        return None
    return new_aluno


def consulta_aluno(dicionario:dict) -> Aluno:
    ...


def deleta_aluno() -> None:
    ...


def altera_aluno() -> Aluno:
    ...
