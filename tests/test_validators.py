"""
test_validators.py
------------------
Testes unitarios das regras de validacao (modulo src/validators.py).
"""

import pytest

from src.validators import validar_dados_tarefa, ErroDeValidacao, TAMANHO_MAXIMO_TITULO


def test_titulo_valido_e_normalizado():
    # Espacos nas pontas devem ser removidos.
    resultado = validar_dados_tarefa({"titulo": "  Configurar servidor  "})
    assert resultado["titulo"] == "Configurar servidor"


def test_titulo_obrigatorio_na_criacao():
    with pytest.raises(ErroDeValidacao):
        validar_dados_tarefa({"descricao": "sem titulo"})


def test_titulo_vazio_e_invalido():
    with pytest.raises(ErroDeValidacao):
        validar_dados_tarefa({"titulo": "   "})


def test_titulo_muito_longo_e_invalido():
    titulo_grande = "a" * (TAMANHO_MAXIMO_TITULO + 1)
    with pytest.raises(ErroDeValidacao):
        validar_dados_tarefa({"titulo": titulo_grande})


def test_status_invalido_e_rejeitado():
    with pytest.raises(ErroDeValidacao):
        validar_dados_tarefa({"titulo": "Tarefa", "status": "inexistente"})


def test_prioridade_invalida_e_rejeitada():
    with pytest.raises(ErroDeValidacao):
        validar_dados_tarefa({"titulo": "Tarefa", "prioridade": "urgentissima"})


def test_status_e_prioridade_validos_sao_aceitos():
    resultado = validar_dados_tarefa(
        {"titulo": "Tarefa", "status": "em_progresso", "prioridade": "alta"}
    )
    assert resultado["status"] == "em_progresso"
    assert resultado["prioridade"] == "alta"


def test_validacao_parcial_permite_titulo_ausente():
    # Em updates (parcial=True), o titulo nao e obrigatorio.
    resultado = validar_dados_tarefa({"status": "concluido"}, parcial=True)
    assert resultado == {"status": "concluido"}
