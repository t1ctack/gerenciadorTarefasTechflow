"""
Gera os dois diagramas UML obrigatorios do trabalho:
  - diagrama_casos_de_uso.png
  - diagrama_classes.png
Usa apenas matplotlib (sem dependencias externas de binarios).
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, Rectangle, FancyArrowPatch
import os

AZUL = "#2563eb"
AZUL_ESCURO = "#1e3a8a"
CINZA = "#475569"
FUNDO_BOX = "#eef2f7"

OUT = os.path.dirname(__file__)


def ator(ax, x, y, nome):
    """Desenha um ator (boneco-palito) da UML."""
    ax.add_patch(plt.Circle((x, y + 0.55), 0.16, fill=False, lw=1.8, color=CINZA))
    ax.plot([x, x], [y + 0.39, y - 0.15], color=CINZA, lw=1.8)        # tronco
    ax.plot([x - 0.28, x + 0.28], [y + 0.2, y + 0.2], color=CINZA, lw=1.8)  # bracos
    ax.plot([x, x - 0.22], [y - 0.15, y - 0.6], color=CINZA, lw=1.8)  # perna esq
    ax.plot([x, x + 0.22], [y - 0.15, y - 0.6], color=CINZA, lw=1.8)  # perna dir
    ax.text(x, y - 0.85, nome, ha="center", va="top", fontsize=10, fontweight="bold")


def caso_uso(ax, x, y, texto, w=2.6, h=0.78):
    """Desenha uma elipse de caso de uso."""
    ax.add_patch(Ellipse((x, y), w, h, facecolor="#dbeafe", edgecolor=AZUL, lw=1.5))
    ax.text(x, y, texto, ha="center", va="center", fontsize=9.5)


def liga(ax, x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color=CINZA, lw=1.0, zorder=0)


# ============================================================ DIAGRAMA 1
def gerar_casos_de_uso():
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis("off")

    ax.text(7, 8.6, "Diagrama de Casos de Uso", ha="center",
            fontsize=15, fontweight="bold", color=AZUL_ESCURO)
    ax.text(7, 8.15, "Sistema de Gerenciamento de Tarefas Agil - TechFlow",
            ha="center", fontsize=10, color=CINZA)

    # Fronteira do sistema
    ax.add_patch(Rectangle((4.3, 0.8), 5.4, 6.6, fill=False, lw=1.6, color=AZUL_ESCURO))
    ax.text(7, 7.15, "Sistema de Gerenciamento de Tarefas", ha="center",
            fontsize=10, fontweight="bold", color=AZUL_ESCURO)

    # Atores
    ator(ax, 1.6, 4.7, "Gestor de\nProjetos")
    ator(ax, 12.4, 4.7, "Membro da\nEquipe")

    # Casos de uso (dentro da fronteira)
    casos = [
        (7, 6.3, "Criar Tarefa"),
        (7, 5.3, "Listar Tarefas"),
        (7, 4.3, "Atualizar / Mover Tarefa"),
        (7, 3.3, "Buscar / Filtrar Tarefas"),
        (7, 2.3, "Excluir Tarefa"),
        (7, 1.4, "Acompanhar Quadro Kanban"),
    ]
    for x, y, t in casos:
        caso_uso(ax, x, y, t)

    # Ligacoes do Gestor (todos os casos)
    for _, y, _ in casos:
        liga(ax, 2.0, 4.4, 5.7, y)
    # Ligacoes do Membro da Equipe (subconjunto)
    for _, y, _ in [casos[1], casos[2], casos[3], casos[5]]:
        liga(ax, 12.0, 4.4, 8.3, y)

    plt.tight_layout()
    caminho = os.path.join(OUT, "diagrama_casos_de_uso.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()
    print("ok:", caminho)


# ============================================================ DIAGRAMA 2
def classe(ax, x, y, w, titulo, atributos, metodos):
    """Desenha uma classe UML (3 compartimentos)."""
    lh = 0.34
    h_attr = max(len(atributos), 1) * lh
    h_met = max(len(metodos), 1) * lh
    h_total = 0.5 + h_attr + h_met

    topo = y
    # corpo
    ax.add_patch(Rectangle((x, topo - h_total), w, h_total,
                           facecolor="white", edgecolor=AZUL_ESCURO, lw=1.5))
    # cabecalho
    ax.add_patch(Rectangle((x, topo - 0.5), w, 0.5,
                           facecolor=AZUL, edgecolor=AZUL_ESCURO, lw=1.5))
    ax.text(x + w / 2, topo - 0.25, titulo, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color="white")

    # atributos
    y_attr = topo - 0.5
    ax.plot([x, x + w], [y_attr, y_attr], color=AZUL_ESCURO, lw=1.2)
    for i, a in enumerate(atributos):
        ax.text(x + 0.12, y_attr - 0.2 - i * lh, a, ha="left", va="center", fontsize=8.3)

    # metodos
    y_met = y_attr - h_attr
    ax.plot([x, x + w], [y_met, y_met], color=AZUL_ESCURO, lw=1.2)
    for i, m in enumerate(metodos):
        ax.text(x + 0.12, y_met - 0.2 - i * lh, m, ha="left", va="center", fontsize=8.3)

    return (x, topo, w, h_total)


def gerar_classes():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 11)
    ax.axis("off")

    ax.text(7.5, 10.6, "Diagrama de Classes", ha="center",
            fontsize=15, fontweight="bold", color=AZUL_ESCURO)
    ax.text(7.5, 10.15, "Sistema de Gerenciamento de Tarefas Agil - TechFlow",
            ha="center", fontsize=10, color=CINZA)

    # AppFlask
    classe(ax, 0.5, 9.4, 4.2, "AppFlask (app.py)",
           ["+ repo: RepositorioTarefas"],
           ["+ listar_tarefas()", "+ criar_tarefa()", "+ obter_tarefa()",
            "+ atualizar_tarefa()", "+ deletar_tarefa()"])

    # RepositorioTarefas
    classe(ax, 5.6, 9.4, 4.6, "RepositorioTarefas",
           ["- conn: Connection", "- db_path: str"],
           ["+ criar(dados): Tarefa", "+ listar(status): list",
            "+ obter(id): Tarefa", "+ buscar(texto,...): list",
            "+ atualizar(id, dados)", "+ deletar(id): bool"])

    # Validador
    classe(ax, 11.0, 9.4, 3.7, "Validador (validators)",
           ["+ STATUS_VALIDOS", "+ PRIORIDADES_VALIDAS"],
           ["+ validar_dados_tarefa()", "  -> ErroDeValidacao"])

    # Tarefa
    classe(ax, 5.6, 4.6, 4.6, "Tarefa",
           ["+ id: int", "+ titulo: str", "+ descricao: str",
            "+ status: str", "+ prioridade: str", "+ criado_em: str"],
           ["+ to_dict(): dict", "+ from_row(row): Tarefa"])

    # Relacionamentos (setas)
    # App --> Repositorio (associacao / dependencia)
    ax.add_patch(FancyArrowPatch((4.7, 8.0), (5.6, 8.0),
                 arrowstyle="-|>", mutation_scale=14, color=CINZA, lw=1.3))
    ax.text(5.15, 8.18, "usa", fontsize=8, color=CINZA, ha="center")

    # Repositorio --> Validador (dependencia)
    ax.add_patch(FancyArrowPatch((10.2, 8.2), (11.0, 8.2),
                 arrowstyle="-|>", mutation_scale=14, color=CINZA, lw=1.3,
                 linestyle="--"))
    ax.text(10.6, 8.4, "valida", fontsize=8, color=CINZA, ha="center")

    # Repositorio --> Tarefa (cria/gerencia - associacao)
    ax.add_patch(FancyArrowPatch((7.9, 6.05), (7.9, 4.95),
                 arrowstyle="-|>", mutation_scale=14, color=CINZA, lw=1.3))
    ax.text(8.55, 5.5, "cria / gerencia", fontsize=8, color=CINZA, ha="left")

    plt.tight_layout()
    caminho = os.path.join(OUT, "diagrama_classes.png")
    plt.savefig(caminho, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close()
    print("ok:", caminho)


if __name__ == "__main__":
    gerar_casos_de_uso()
    gerar_classes()
