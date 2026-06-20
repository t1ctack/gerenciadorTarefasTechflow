"""
app.py
------
Aplicacao web (Flask) que expoe a API REST de tarefas e serve a interface.

Endpoints:
    GET    /                      -> pagina HTML (interface Kanban)
    GET    /api/tarefas           -> lista tarefas (aceita ?status=, ?prioridade=, ?busca=)
    POST   /api/tarefas           -> cria uma tarefa
    GET    /api/tarefas/<id>      -> obtem uma tarefa
    PUT    /api/tarefas/<id>      -> atualiza uma tarefa
    DELETE /api/tarefas/<id>      -> remove uma tarefa
"""

from flask import Flask, jsonify, request, render_template

from src.repository import RepositorioTarefas
from src.validators import ErroDeValidacao


def criar_app(db_path: str = "tarefas.db") -> Flask:
    """
    Application factory: cria e configura a instancia do Flask.

    Receber o caminho do banco por parametro permite que os testes usem um
    banco em memoria isolado, sem afetar o banco real.
    """
    app = Flask(__name__)
    repo = RepositorioTarefas(db_path)

    # Disponibiliza o repositorio para os testes acessarem, se precisarem.
    app.config["REPO"] = repo

    # -------------------------------------------------------------- Interface
    @app.route("/")
    def index():
        return render_template("index.html")

    # -------------------------------------------------------------- API REST
    @app.route("/api/tarefas", methods=["GET"])
    def listar_tarefas():
        busca = request.args.get("busca")
        status = request.args.get("status")
        prioridade = request.args.get("prioridade")
        # Se houver qualquer filtro, usa busca(); senao, lista tudo.
        if busca or status or prioridade:
            tarefas = repo.buscar(texto=busca, status=status, prioridade=prioridade)
        else:
            tarefas = repo.listar()
        return jsonify([t.to_dict() for t in tarefas])

    @app.route("/api/tarefas", methods=["POST"])
    def criar_tarefa():
        try:
            tarefa = repo.criar(request.get_json(silent=True) or {})
            return jsonify(tarefa.to_dict()), 201
        except ErroDeValidacao as erro:
            return jsonify({"erro": str(erro)}), 400

    @app.route("/api/tarefas/<int:tarefa_id>", methods=["GET"])
    def obter_tarefa(tarefa_id):
        tarefa = repo.obter(tarefa_id)
        if tarefa is None:
            return jsonify({"erro": "Tarefa nao encontrada."}), 404
        return jsonify(tarefa.to_dict())

    @app.route("/api/tarefas/<int:tarefa_id>", methods=["PUT"])
    def atualizar_tarefa(tarefa_id):
        try:
            tarefa = repo.atualizar(tarefa_id, request.get_json(silent=True) or {})
            if tarefa is None:
                return jsonify({"erro": "Tarefa nao encontrada."}), 404
            return jsonify(tarefa.to_dict())
        except ErroDeValidacao as erro:
            return jsonify({"erro": str(erro)}), 400

    @app.route("/api/tarefas/<int:tarefa_id>", methods=["DELETE"])
    def deletar_tarefa(tarefa_id):
        if repo.deletar(tarefa_id):
            return jsonify({"mensagem": "Tarefa removida com sucesso."})
        return jsonify({"erro": "Tarefa nao encontrada."}), 404

    return app


# Permite rodar com "python -m src.app" ou "python src/app.py".
if __name__ == "__main__":
    aplicacao = criar_app()
    aplicacao.run(debug=True, host="0.0.0.0", port=5000)
