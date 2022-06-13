import pytest
from unittest.mock import MagicMock, patch
from professores import services
from professores.models import Professor
class TestProfessorServices:

    @patch("professores.services.Professor")
    def test_create_professor(self, professor_mock):
        profe = Professor()
        new_professor = services.cria_professor(profe)
        professor_mock.save.has_been_called()
