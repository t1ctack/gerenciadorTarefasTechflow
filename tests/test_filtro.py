"""
test_filtro.py
--------------
Testes da funcionalidade de BUSCA e FILTRO de tarefas.

Esses testes cobrem a funcionalidade adicionada na MUDANCA DE ESCOPO do projeto
(metodo repo.buscar() e parametros de filtro no endpoint GET /api/tarefas).
"""


def test_buscar_por_texto_no_titulo(repo):
    repo.criar({"titulo": "Entregar carga no porto"})
    repo.criar({"titulo": "Reuniao com cliente"})
    resultado = repo.buscar(texto="carga")
    assert len(resultado) == 1
    assert resultado[0].titulo == "Entregar carga no porto"


def test_buscar_por_prioridade(repo):
    repo.criar({"titulo": "Urgente", "prioridade": "alta"})
    repo.criar({"titulo": "Normal", "prioridade": "media"})
    resultado = repo.buscar(prioridade="alta")
    assert len(resultado) == 1
    assert resultado[0].titulo == "Urgente"


def test_buscar_combinando_status_e_prioridade(repo):
    repo.criar({"titulo": "A", "status": "em_progresso", "prioridade": "alta"})
    repo.criar({"titulo": "B", "status": "a_fazer", "prioridade": "alta"})
    resultado = repo.buscar(status="em_progresso", prioridade="alta")
    assert len(resultado) == 1
    assert resultado[0].titulo == "A"


def test_filtro_via_api(cliente):
    cliente.post("/api/tarefas", json={"titulo": "Critica", "prioridade": "alta"})
    cliente.post("/api/tarefas", json={"titulo": "Comum", "prioridade": "baixa"})
    resp = cliente.get("/api/tarefas?prioridade=alta")
    assert resp.status_code == 200
    dados = resp.get_json()
    assert len(dados) == 1
    assert dados[0]["titulo"] == "Critica"


def test_busca_via_api(cliente):
    cliente.post("/api/tarefas", json={"titulo": "Rastrear entrega"})
    cliente.post("/api/tarefas", json={"titulo": "Pagar fornecedor"})
    resp = cliente.get("/api/tarefas?busca=entrega")
    assert len(resp.get_json()) == 1
