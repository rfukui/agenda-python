import pytest
from unittest.mock import MagicMock, patch
from professores import services
from professores.models import Professor
from datetime import datetime


class TestProfessorServices:

    @patch("professores.services.Professor")
    def test_create_professor(self, professor_mock):
        professor_mock.save = MagicMock(return_value=Professor)
        profe = {"name": "pedro", }

        services.cria_professor(profe)

        professor_mock.assert_called_once_with(profe)
        professor_mock().save.assert_called_once()

    @patch("professores.services.Professor")
    def test_create_teste_professor(self, professor_mock):
        professor_mock.save = MagicMock(return_value=Professor)
        profe = {"name": "teste", }

        services.cria_professor(profe)

        professor_mock.assert_called_once_with(profe)
        professor_mock().save.assert_not_called()

    @patch("professores.services.Professor", return_value=MagicMock())
    def test_error(self, professor_mock):
        return_instance = MagicMock()
        professor_mock.return_value = return_instance
        return_instance.save.side_effect = KeyError('foo')
        profe = {"name": "Pedro", }

        new_professor = services.cria_professor(profe)

        professor_mock.assert_called_once_with(profe)
        return_instance.save.assert_called_once()
        print(new_professor)
        assert new_professor is None

@patch("professores.services.ProfessorSchedulle")
class TestProfessorSchedulle:

    @patch("professores.services.consulta_professor")
    def test_criar_horario_professor_existente(self, consulta_professor_mock, schedulle_mock):
        consulta_professor_mock.return_value = Professor()
        services.cria_agenda_professor(dict(professor_id=5))
        consulta_professor_mock.assert_called_once()
        schedulle_mock.create.assert_called_once()

    @patch("professores.services.consulta_professor")
    def test_criar_horario_professor_inexistente(self, consulta_professor_mock, schedulle_mock):
        consulta_professor_mock.return_value = None
        services.cria_agenda_professor(dict(professor_id=5))
        consulta_professor_mock.assert_called_once()
        schedulle_mock.create.assert_not_called()

    @patch("professores.services.consulta_professor")
    @patch("professores.services._verifica_colisao_agenda")
    def test_criar_horario_professor_agenda_disponivel(self, colisao_mock, consulta_professor_mock, schedulle_mock):
        colisao_mock.return_value = True
        consulta_professor_mock.return_value = dict(professor_id=5, schedulles=[])
        prof_dict = dict(professor_id=5, start_time=datetime.now(), stop_time=datetime.now(), week_day=2)
        services.cria_agenda_professor(prof_dict)
        consulta_professor_mock.assert_called_once()
        schedulle_mock.create.assert_called_once()
        colisao_mock.assert_called_once()
















