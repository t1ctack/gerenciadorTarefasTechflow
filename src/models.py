"""
models.py
---------
Define a estrutura de dados (modelo) de uma Tarefa do sistema.

Em projetos maiores este arquivo costuma usar um ORM (SQLAlchemy, Django ORM
etc.). Para manter o projeto simples e didatico, usamos uma classe Python pura
(dataclass) que representa uma Tarefa e sabe se converter para/de dicionario.
"""

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional

# Valores permitidos para o campo "status" (colunas do Kanban).
STATUS_VALIDOS = ("a_fazer", "em_progresso", "concluido")

# Valores permitidos para o campo "prioridade".
PRIORIDADES_VALIDAS = ("baixa", "media", "alta")


@dataclass
class Tarefa:
    """Representa uma tarefa no sistema de gerenciamento."""

    titulo: str
    descricao: str = ""
    status: str = "a_fazer"
    prioridade: str = "media"
    id: Optional[int] = None
    # Data de criacao em formato ISO. Gerada automaticamente quando nao informada.
    criado_em: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_dict(self) -> dict:
        """Converte a tarefa em um dicionario (util para devolver JSON na API)."""
        return asdict(self)

    @staticmethod
    def from_row(row) -> "Tarefa":
        """Cria uma Tarefa a partir de uma linha (sqlite3.Row) do banco de dados."""
        return Tarefa(
            id=row["id"],
            titulo=row["titulo"],
            descricao=row["descricao"],
            status=row["status"],
            prioridade=row["prioridade"],
            criado_em=row["criado_em"],
        )
