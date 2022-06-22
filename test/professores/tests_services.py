import pytest
from unittest.mock import MagicMock, patch
from professores import services


class TestProfessorServices:

    @patch("professores.services.Professor")
    def test_create_professor(self, professor_mock):
        professor_mock.save = MagicMock()
        profe = {}

        services.cria_professor(profe)

        professor_mock.assert_called_once_with({})
        professor_mock().save.assert_called_once()
