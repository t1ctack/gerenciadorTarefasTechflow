"""
repository.py
-------------
Camada de acesso a dados (Repository Pattern).

Encapsula toda a comunicacao com o banco SQLite, expondo metodos de alto nivel
para o CRUD de tarefas (Create, Read, Update, Delete). Manter o acesso ao banco
isolado aqui permite trocar a tecnologia de armazenamento sem mexer na API e
facilita os testes (usamos um banco em memoria nos testes).
"""

import sqlite3
from typing import List, Optional

from src.models import Tarefa
from src.validators import validar_dados_tarefa, ErroDeValidacao


class RepositorioTarefas:
    """Repositorio responsavel por persistir e recuperar tarefas no SQLite."""

    def __init__(self, db_path: str = "tarefas.db"):
        # check_same_thread=False permite uso com o servidor de desenvolvimento Flask.
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._criar_tabela()

    def _criar_tabela(self) -> None:
        """Cria a tabela de tarefas caso ainda nao exista."""
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tarefas (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo     TEXT NOT NULL,
                descricao  TEXT DEFAULT '',
                status     TEXT NOT NULL DEFAULT 'a_fazer',
                prioridade TEXT NOT NULL DEFAULT 'media',
                criado_em  TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    # ------------------------------------------------------------------ CREATE
    def criar(self, dados: dict) -> Tarefa:
        """Valida os dados e insere uma nova tarefa, devolvendo-a com o id gerado."""
        limpo = validar_dados_tarefa(dados, parcial=False)
        tarefa = Tarefa(
            titulo=limpo["titulo"],
            descricao=limpo.get("descricao", ""),
            status=limpo.get("status", "a_fazer"),
            prioridade=limpo.get("prioridade", "media"),
        )
        cursor = self.conn.execute(
            "INSERT INTO tarefas (titulo, descricao, status, prioridade, criado_em) "
            "VALUES (?, ?, ?, ?, ?)",
            (tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.prioridade, tarefa.criado_em),
        )
        self.conn.commit()
        tarefa.id = cursor.lastrowid
        return tarefa

    # -------------------------------------------------------------------- READ
    def listar(self, status: Optional[str] = None) -> List[Tarefa]:
        """Lista todas as tarefas, opcionalmente filtrando por status."""
        if status:
            rows = self.conn.execute(
                "SELECT * FROM tarefas WHERE status = ? ORDER BY id", (status,)
            ).fetchall()
        else:
            rows = self.conn.execute("SELECT * FROM tarefas ORDER BY id").fetchall()
        return [Tarefa.from_row(r) for r in rows]

    def obter(self, tarefa_id: int) -> Optional[Tarefa]:
        """Retorna uma tarefa pelo id, ou None se nao existir."""
        row = self.conn.execute(
            "SELECT * FROM tarefas WHERE id = ?", (tarefa_id,)
        ).fetchone()
        return Tarefa.from_row(row) if row else None

    def buscar(
        self,
        texto: Optional[str] = None,
        status: Optional[str] = None,
        prioridade: Optional[str] = None,
    ) -> List[Tarefa]:
        """
        Busca/filtra tarefas combinando texto (titulo ou descricao), status e
        prioridade. Funcionalidade adicionada na MUDANCA DE ESCOPO do projeto.
        """
        consulta = "SELECT * FROM tarefas WHERE 1 = 1"
        parametros = []
        if texto:
            consulta += " AND (titulo LIKE ? OR descricao LIKE ?)"
            termo = f"%{texto}%"
            parametros.extend([termo, termo])
        if status:
            consulta += " AND status = ?"
            parametros.append(status)
        if prioridade:
            consulta += " AND prioridade = ?"
            parametros.append(prioridade)
        consulta += " ORDER BY id"
        rows = self.conn.execute(consulta, parametros).fetchall()
        return [Tarefa.from_row(r) for r in rows]

    # ------------------------------------------------------------------ UPDATE
    def atualizar(self, tarefa_id: int, dados: dict) -> Optional[Tarefa]:
        """Atualiza os campos informados de uma tarefa existente."""
        if self.obter(tarefa_id) is None:
            return None
        limpo = validar_dados_tarefa(dados, parcial=True)
        if not limpo:
            raise ErroDeValidacao("Nenhum campo valido foi enviado para atualizacao.")
        colunas = ", ".join(f"{campo} = ?" for campo in limpo)
        valores = list(limpo.values()) + [tarefa_id]
        self.conn.execute(f"UPDATE tarefas SET {colunas} WHERE id = ?", valores)
        self.conn.commit()
        return self.obter(tarefa_id)

    # ------------------------------------------------------------------ DELETE
    def deletar(self, tarefa_id: int) -> bool:
        """Remove uma tarefa. Retorna True se algo foi removido."""
        cursor = self.conn.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def fechar(self) -> None:
        """Fecha a conexao com o banco."""
        self.conn.close()
