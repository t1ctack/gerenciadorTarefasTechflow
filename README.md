# 🗂️ Gerenciador de Tarefas Ágil — TechFlow Solutions

Sistema web de gerenciamento de tarefas baseado em metodologias ágeis, desenvolvido como projeto da disciplina de **Engenharia de Software**.

> **Caso:** A *TechFlow Solutions* foi contratada por uma **startup de logística** para criar um sistema que permita acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

---

## 🎯 Objetivo

Disponibilizar um sistema simples e funcional que permita à equipe **criar, visualizar, atualizar, mover e excluir tarefas** organizadas em um quadro **Kanban** (A Fazer → Em Progresso → Concluído), aplicando na prática os conceitos de Engenharia de Software: modelagem, versionamento, desenvolvimento ágil, automação de testes e documentação.

## 📌 Escopo

- CRUD completo de tarefas (Create, Read, Update, Delete).
- Cada tarefa possui título, descrição, **status** (coluna do Kanban) e **prioridade**.
- Interface web em formato de quadro Kanban com três colunas.
- API REST consumida pela interface.

## 🔄 Metodologia adotada — Kanban

O projeto utiliza **Kanban**, método ágil ideal para fluxo contínuo de tarefas. O quadro do **GitHub Projects** organiza o trabalho em três colunas — **A Fazer**, **Em Progresso** e **Concluído** — permitindo visualizar o andamento em tempo real, limitar o trabalho em progresso e identificar gargalos.

---

## 🧱 Estrutura de diretórios

```
.
├── README.md
├── requirements.txt
├── pytest.ini
├── .github/workflows/ci.yml   # Pipeline de CI (GitHub Actions)
├── src/                       # Código-fonte
│   ├── models.py
│   ├── validators.py
│   ├── repository.py
│   ├── app.py
│   ├── templates/index.html
│   └── static/ (style.css, script.js)
├── tests/                     # Testes automatizados (PyTest)
└── docs/                      # Documentação e diagramas UML
```

---

## ▶️ Como executar

**Pré-requisitos:** Python 3.10 ou superior.

```bash
pip install -r requirements.txt
python -m src.app
```

Acesse **http://localhost:5000** no navegador.

## ✅ Testes automatizados

```bash
pytest -v
```

## 🔁 Integração Contínua (CI)

O arquivo `.github/workflows/ci.yml` configura um pipeline no **GitHub Actions** que roda lint e testes automaticamente a cada `push` ou `pull request`.

---

## 🛠️ Tecnologias

Python 3 · Flask · SQLite · PyTest · GitHub Actions · GitHub Projects (Kanban)

## 👤 Autor

Projeto desenvolvido para a disciplina de **Engenharia de Software** — UniFECAF.
