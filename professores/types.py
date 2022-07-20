from dataclasses import dataclass

from typing import Optional

@dataclass
class InputProfessor:
    nome: str
    disciplina: str
    modelo_trabalho: Optional[str]
