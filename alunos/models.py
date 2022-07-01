from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    curso = Column(String(20), nullable=False)

    def __repr__(self):
        return "<User(Nome='%s', Curso='%s')>" % (
            self.nome, self.curso)

class AlunoSchedulle(Base):
    __tablename__ = 'agenda_alunos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    start_time = Column(DateTime)
    stop_time = Column(DateTime)
    week_day = Column(Integer)
