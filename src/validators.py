"""
validators.py
-------------
Funcoes de validacao das entradas de uma tarefa.

Centralizar a validacao em um modulo proprio facilita os testes automatizados
e mantem as regras de negocio separadas da API (app.py) e do banco
(repository.py). Esse e um dos pontos avaliados pelo pipeline de testes.
"""

from src.models import STATUS_VALIDOS, PRIORIDADES_VALIDAS

# Tamanho maximo permitido para o titulo de uma tarefa.
TAMANHO_MAXIMO_TITULO = 120


class ErroDeValidacao(Exception):
    """Excecao lancada quando os dados de uma tarefa sao invalidos."""


def validar_dados_tarefa(dados: dict, parcial: bool = False) -> dict:
    """
    Valida e normaliza os dados recebidos para criar/atualizar uma tarefa.

    Parametros:
        dados   -- dicionario com os campos enviados pelo usuario.
        parcial -- quando True (usado em updates), campos ausentes sao ignorados;
                   quando False (usado na criacao), o titulo e obrigatorio.

    Retorna um dicionario apenas com os campos validos e normalizados.
    Lanca ErroDeValidacao quando algum campo e invalido.
    """
    if not isinstance(dados, dict):
        raise ErroDeValidacao("Os dados enviados devem estar em formato de objeto/JSON.")

    limpo = {}

    # --- Titulo ---------------------------------------------------------
    if "titulo" in dados:
        titulo = (dados.get("titulo") or "").strip()
        if not titulo:
            raise ErroDeValidacao("O titulo da tarefa nao pode ficar vazio.")
        if len(titulo) > TAMANHO_MAXIMO_TITULO:
            raise ErroDeValidacao(
                f"O titulo deve ter no maximo {TAMANHO_MAXIMO_TITULO} caracteres."
            )
        limpo["titulo"] = titulo
    elif not parcial:
        # Na criacao o titulo e obrigatorio.
        raise ErroDeValidacao("O campo 'titulo' e obrigatorio.")

    # --- Descricao ------------------------------------------------------
    if "descricao" in dados:
        limpo["descricao"] = (dados.get("descricao") or "").strip()

    # --- Status ---------------------------------------------------------
    if "status" in dados:
        status = (dados.get("status") or "").strip()
        if status not in STATUS_VALIDOS:
            raise ErroDeValidacao(
                f"Status invalido. Use um destes: {', '.join(STATUS_VALIDOS)}."
            )
        limpo["status"] = status

    # --- Prioridade -----------------------------------------------------
    if "prioridade" in dados:
        prioridade = (dados.get("prioridade") or "").strip()
        if prioridade not in PRIORIDADES_VALIDAS:
            raise ErroDeValidacao(
                f"Prioridade invalida. Use uma destas: {', '.join(PRIORIDADES_VALIDAS)}."
            )
        limpo["prioridade"] = prioridade

    return limpo
