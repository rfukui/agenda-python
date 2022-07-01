import pytest
from unittest.mock import MagicMock, patch
from alunos import services
from alunos.models import Aluno


class TestAlunoServices:

    @patch("alunos.services.Aluno")
    def test_create_aluno(self, aluno_mock):
        aluno_mock.save = MagicMock(return_value=Aluno)
        aluno = {"name": "joao", }

        services.cria_aluno(aluno)

        aluno_mock.assert_called_once_with(aluno)
        aluno_mock().save.assert_called_once()

    @patch("alunos.services.Aluno")
    def test_create_teste_aluno(self, aluno_mock):
        aluno_mock.save = MagicMock(return_value=Aluno)
        aluno = {"name": "teste", }

        services.cria_aluno(aluno)

        aluno_mock.assert_called_once_with(aluno)
        aluno_mock().save.assert_not_called()

    @patch("alunos.services.Aluno")
    def test_error(self, aluno_mock):
        aluno_mock.save.side_effect = KeyError('foo')
        aluno = {"name": "Joao", }

        new_professor = services.cria_aluno(aluno)

        aluno_mock.assert_called_once_with(aluno)
        aluno_mock().save.assert_called_once()
        assert new_professor is None