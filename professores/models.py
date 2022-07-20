from typing import List
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import create_engine
from .types import InputProfessor

Base = declarative_base()
engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


class ProfessorSchedulle(Base):
    __tablename__ = 'agenda_professores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    professor = relationship('Professor')
    start_time = Column(DateTime)
    stop_time = Column(DateTime)
    week_day = Column(Integer)


class Professor(Base):
    __tablename__ = 'professores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    disciplina = Column(String(20), nullable=False)
    modelo_trabalho = Column(String(10), nullable=False)
    schedulles = relationship(ProfessorSchedulle, backref='professores')

    def save(self):
        session.commit()

    def __repr__(self):
        return "<User(Nome='%s', Disciplina='%s', Modelo de Trabalho='%s')>" % (
            self.nome, self.disciplina, self.modelo_trabalho)

    @staticmethod
    def get_all():
        return session.query(Professor).all()

    @staticmethod
    def get(_id: int) -> 'Professor':
        prof = session.query(Professor).filter(id == _id).first()
        print(prof)
        return prof


    @staticmethod
    def create(professor: InputProfessor) -> 'Professor':
        new_professor = Professor()
        new_professor.nome=professor.nome
        session.add(new_professor)
        session.commit()
        return new_professor


Base.metadata.create_all(engine)
