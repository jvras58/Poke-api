from io import StringIO

import pytest


@pytest.fixture
def mock_input(monkeypatch):
    """
    Fixture que simula a entrada do usuário, substituindo o fluxo de entrada padrão.

    Args:
        monkeypatch: Objeto utilizado para substituir o fluxo de entrada padrão.

    returns:
        StringIO: A StringIO object representing the user input stream.
    """
    user_input = StringIO()
    monkeypatch.setattr('sys.stdin', user_input)
    return user_input
