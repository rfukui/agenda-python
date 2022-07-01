from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
Base = declarative_base()


class Professor(Base):
    __tablename__ = 'professores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    disciplina = Column(String(20), nullable=False)
    modelo_trabalho = Column(String(10), nullable=False)

    def save(self):
        ...

    def __repr__(self):
        return "<User(Nome='%s', Disciplina='%s', Modelo de Trabalho='%s')>" % (
            self.nome, self.disciplina, self.modelo_trabalho)


class ProfessorSchedulle(Base):
    __tablename__ = 'agenda_professores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    start_time = Column(DateTime)
    stop_time = Column(DateTime)
    week_day = Column(Integer)
