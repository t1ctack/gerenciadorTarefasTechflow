"""
test_repository.py
------------------
Testes do CRUD na camada de repositorio (src/repository.py).
"""

import pytest

from src.validators import ErroDeValidacao


def test_criar_e_obter_tarefa(repo):
    tarefa = repo.criar({"titulo": "Modelar banco de dados"})
    assert tarefa.id is not None
    obtida = repo.obter(tarefa.id)
    assert obtida.titulo == "Modelar banco de dados"
    assert obtida.status == "a_fazer"          # valor padrao
    assert obtida.prioridade == "media"        # valor padrao


def test_listar_tarefas(repo):
    repo.criar({"titulo": "Tarefa 1"})
    repo.criar({"titulo": "Tarefa 2"})
    tarefas = repo.listar()
    assert len(tarefas) == 2


def test_listar_filtrando_por_status(repo):
    repo.criar({"titulo": "Pendente"})
    repo.criar({"titulo": "Feita", "status": "concluido"})
    concluidas = repo.listar(status="concluido")
    assert len(concluidas) == 1
    assert concluidas[0].titulo == "Feita"


def test_atualizar_tarefa(repo):
    tarefa = repo.criar({"titulo": "Escrever testes"})
    atualizada = repo.atualizar(tarefa.id, {"status": "em_progresso"})
    assert atualizada.status == "em_progresso"


def test_atualizar_tarefa_inexistente_retorna_none(repo):
    assert repo.atualizar(9999, {"status": "concluido"}) is None


def test_atualizar_sem_campos_validos_gera_erro(repo):
    tarefa = repo.criar({"titulo": "Tarefa"})
    with pytest.raises(ErroDeValidacao):
        repo.atualizar(tarefa.id, {"campo_inexistente": "x"})


def test_deletar_tarefa(repo):
    tarefa = repo.criar({"titulo": "Remover depois"})
    assert repo.deletar(tarefa.id) is True
    assert repo.obter(tarefa.id) is None


def test_deletar_tarefa_inexistente_retorna_false(repo):
    assert repo.deletar(9999) is False


def test_criar_tarefa_sem_titulo_gera_erro(repo):
    with pytest.raises(ErroDeValidacao):
        repo.criar({"descricao": "sem titulo"})
