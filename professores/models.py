from datetime import datetime
from typing import List
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select
from sqlalchemy import create_engine
from .types import InputProfessor
from dataclasses import asdict

Base = declarative_base()
engine = create_engine('sqlite:///test.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()


class ProfessorSchedule(Base):
    __tablename__ = 'agenda_professores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    professor = relationship('Professor')
    start_time = Column(DateTime)
    stop_time = Column(DateTime)
    week_day = Column(Integer)

    @staticmethod
    def create(schedule: dict) ->'ProfessorSchedule':
        new_professor_schedule = ProfessorSchedule()
        for k, v in schedule.items():
            setattr(new_professor_schedule, k, v)
        new_professor_schedule.start_time = datetime.strptime(new_professor_schedule.start_time, '%H:%M')
        new_professor_schedule.stop_time = datetime.strptime(new_professor_schedule.stop_time, '%H:%M')
        session.add(new_professor_schedule)
        print(new_professor_schedule)
        return new_professor_schedule

    # @staticmethod
    def save(self):
        session.commit()

    def __repr__(self):
        return "<ProfessorSchedule(id='%s', professor_id='%s', start_time=%s, stop_time=%s, week_day=%s)>" % (
            self.id, self.professor_id, self.start_time, self.stop_time, self.week_day)


class Professor(Base):
    __tablename__ = 'professores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    disciplina = Column(String(20), nullable=False)
    modelo_trabalho = Column(String(10), nullable=False)
    schedulles = relationship(ProfessorSchedule, backref='professores')

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
        print("dentro")
        prof = session.query(Professor).filter(Professor.id == _id).first()
        print("apos prof")
        return prof

    def update(self, professor: dict) -> 'Professor':
        for k, v in professor.items():
            setattr(self, k, v)
        return self

    def delete(self) ->'Professor':
        session.delete(self)

    @staticmethod
    def create(professor: InputProfessor) -> 'Professor':
        new_professor = Professor()
        new_professor.nome = professor.nome
        new_professor.disciplina = professor.disciplina
        new_professor.modelo_trabalho = professor.modelo_trabalho
        session.add(new_professor)
        session.commit()
        return new_professor

    def dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "disciplina": self.disciplina,
            "modelo_trabalho": self.modelo_trabalho
        }


Base.metadata.create_all(engine)
