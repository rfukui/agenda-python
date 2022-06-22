from .models import Professor


def cria_professor(professor: dict) -> Professor:
    new_professor = Professor(professor)
    new_professor.save()
    return new_professor

def consulta_professor(dicionario:dict) -> Professor:
    ...

def deleta_professor() -> None:
    ...

def altera_professor() -> Professor:
    ...
