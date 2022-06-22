import pytest
from unittest.mock import MagicMock, patch
from professores import services
from professores.models import Professor


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

    @patch("professores.services.Professor")
    def test_error(self, professor_mock):
        professor_mock.save.side_effect = KeyError('foo')
        profe = {"name": "Pedro", }

        new_professor = services.cria_professor(profe)

        professor_mock.assert_called_once_with(profe)
        professor_mock().save.assert_called_once()
        assert new_professor is None
