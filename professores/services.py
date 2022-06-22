from .models import Professor


def cria_professor(professor: dict) -> Professor:
    new_professor = Professor(professor)
    if professor["name"] == "teste":
        return new_professor
    try:
        new_professor.save()
    except Exception:
        return None
    return new_professor


def consulta_professor(dicionario:dict) -> Professor:
    ...


def deleta_professor() -> None:
    ...


def altera_professor() -> Professor:
    ...
