"""
test_api.py
-----------
Testes de integracao da API REST (src/app.py), usando o test_client do Flask.
"""


def test_listar_vazio_retorna_lista(cliente):
    resp = cliente.get("/api/tarefas")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_criar_tarefa_via_api(cliente):
    resp = cliente.post("/api/tarefas", json={"titulo": "Configurar CI"})
    assert resp.status_code == 201
    dados = resp.get_json()
    assert dados["titulo"] == "Configurar CI"
    assert dados["id"] is not None


def test_criar_tarefa_sem_titulo_retorna_400(cliente):
    resp = cliente.post("/api/tarefas", json={"descricao": "x"})
    assert resp.status_code == 400
    assert "erro" in resp.get_json()


def test_obter_tarefa_inexistente_retorna_404(cliente):
    resp = cliente.get("/api/tarefas/9999")
    assert resp.status_code == 404


def test_atualizar_tarefa_via_api(cliente):
    criada = cliente.post("/api/tarefas", json={"titulo": "Tarefa"}).get_json()
    resp = cliente.put(f"/api/tarefas/{criada['id']}", json={"status": "concluido"})
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "concluido"


def test_deletar_tarefa_via_api(cliente):
    criada = cliente.post("/api/tarefas", json={"titulo": "Tarefa"}).get_json()
    resp = cliente.delete(f"/api/tarefas/{criada['id']}")
    assert resp.status_code == 200
    # Apos remover, nao deve mais existir.
    assert cliente.get(f"/api/tarefas/{criada['id']}").status_code == 404


def test_pagina_inicial_carrega(cliente):
    resp = cliente.get("/")
    assert resp.status_code == 200
    assert b"TechFlow" in resp.data
