"""
Ponto de entrada para executar o sistema localmente.

Uso:
    python run.py

Depois, abra o navegador em: http://localhost:5000
"""
from src.app import criar_app

# Cria a aplicacao Flask usando um banco de dados local (arquivo tarefas.db)
app = criar_app("tarefas.db")

if __name__ == "__main__":
    # debug=True facilita o desenvolvimento; em producao deve ser False
    app.run(host="0.0.0.0", port=5000, debug=True)
