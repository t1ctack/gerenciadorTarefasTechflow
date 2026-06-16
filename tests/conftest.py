"""
conftest.py
-----------
Fixtures compartilhadas entre os testes.

Cada teste recebe um repositorio/aplicacao usando um banco SQLite EM MEMORIA
(":memory:"), garantindo que os testes sejam isolados e nao gravem nada em
disco. Isso e fundamental para rodar no pipeline de CI (GitHub Actions).
"""

import pytest

from src.repository import RepositorioTarefas
from src.app import criar_app


@pytest.fixture
def repo():
    """Repositorio com banco em memoria, recriado a cada teste."""
    repositorio = RepositorioTarefas(":memory:")
    yield repositorio
    repositorio.fechar()


@pytest.fixture
def cliente():
    """Cliente de teste do Flask, tambem com banco em memoria."""
    app = criar_app(":memory:")
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c
