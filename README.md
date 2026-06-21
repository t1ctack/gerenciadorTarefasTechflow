# 🗂️ Gerenciador de Tarefas Ágil — TechFlow Solutions

Sistema web de gerenciamento de tarefas baseado em metodologias ágeis, desenvolvido como projeto da disciplina de **Engenharia de Software**.

> **Caso:** A *TechFlow Solutions* foi contratada por uma **startup de logística** para criar um sistema que permita acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

---

## 🎯 Objetivo

Disponibilizar um sistema simples e funcional que permita à equipe **criar, visualizar, atualizar, mover e excluir tarefas** organizadas em um quadro **Kanban** (A Fazer → Em Progresso → Concluído), aplicando na prática os conceitos de Engenharia de Software: modelagem, versionamento, desenvolvimento ágil, automação de testes e gestão de mudanças.

## 📌 Escopo

**Escopo inicial**
- CRUD completo de tarefas (Create, Read, Update, Delete).
- Cada tarefa possui título, descrição, **status** (coluna do Kanban) e **prioridade**.
- Interface web em formato de quadro Kanban com três colunas.
- API REST consumida pela interface.

**Mudança de escopo (descrita na seção [Gestão de Mudanças](#-gestão-de-mudanças))**
- Adição de **busca por texto e filtro por prioridade**.

## 🔄 Metodologia adotada — Kanban

O projeto utiliza **Kanban**, método ágil ideal para fluxo contínuo de tarefas. O quadro do **GitHub Projects** organiza o trabalho em três colunas — **A Fazer**, **Em Progresso** e **Concluído** — permitindo visualizar o andamento em tempo real, limitar o trabalho em progresso e identificar gargalos. A escolha do Kanban (em vez do Scrum) se justifica por ser um projeto de fluxo contínuo, sem sprints fixos, com requisitos que podem mudar ao longo do desenvolvimento — exatamente o cenário de uma startup de logística.

---

## 🧱 Estrutura de diretórios

```
.
├── README.md                  # Este arquivo
├── requirements.txt           # Dependências do projeto
├── pytest.ini                 # Configuração dos testes
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de Integração Contínua (GitHub Actions)
├── src/                       # Código-fonte da aplicação
│   ├── models.py              # Modelo de dados (classe Tarefa)
│   ├── validators.py          # Regras de validação de entradas
│   ├── repository.py          # Camada de acesso a dados (CRUD + busca)
│   ├── app.py                 # API REST + servidor web (Flask)
│   ├── templates/
│   │   └── index.html         # Interface Kanban
│   └── static/
│       ├── style.css
│       └── script.js
├── tests/                     # Testes automatizados (PyTest)
│   ├── conftest.py
│   ├── test_validators.py
│   ├── test_repository.py
│   ├── test_api.py
│   └── test_filtro.py         # Testes da mudança de escopo
└── docs/                      # Documentação e diagramas UML
    ├── KANBAN.md
    ├── gerar_diagramas.py
    ├── diagrama_casos_de_uso.png
    └── diagrama_classes.png
```

---

## ▶️ Como executar o projeto

**Pré-requisitos:** Python 3.10 ou superior.

```bash
# 1. Clonar o repositório
git clone https://github.com/SEU_USUARIO/gerenciador-tarefas-techflow.git
cd gerenciador-tarefas-techflow

# 2. (Opcional) Criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Rodar a aplicação
python run.py
```

Depois acesse **http://localhost:5000** no navegador. 🎉

---

## ✅ Testes automatizados

O projeto possui testes unitários e de integração escritos com **PyTest**:

- `test_validators.py` — regras de validação das entradas.
- `test_repository.py` — operações de CRUD na camada de dados.
- `test_api.py` — integração dos endpoints da API REST.
- `test_filtro.py` — funcionalidade de busca e filtro (mudança de escopo).

Para rodar todos os testes:

```bash
pytest -v
```

## 🔁 Integração Contínua (CI)

O arquivo `.github/workflows/ci.yml` configura um pipeline no **GitHub Actions** que roda automaticamente a cada `push` ou `pull request`. O pipeline:

1. Prepara o ambiente Python.
2. Instala as dependências.
3. Verifica a qualidade do código (lint com `flake8`).
4. Executa todos os testes automatizados (`pytest`).

Assim, nenhum código com testes quebrados é integrado à branch principal, garantindo a **entrega de um software confiável**.

---

## 🔧 Gestão de Mudanças

> **Mudança de escopo:** *Inclusão de busca e filtro de tarefas.*

**Contexto / justificativa:** durante o desenvolvimento, o cliente (startup de logística) relatou que, com o crescimento do número de tarefas, a equipe estava perdendo tempo procurando itens específicos no quadro. Para atender à necessidade de **priorizar tarefas críticas** e localizar tarefas rapidamente, o escopo foi ampliado com uma funcionalidade de **busca por texto** (título/descrição) e **filtro por prioridade**.

**Como foi gerenciada:**
1. Um novo card foi criado na coluna **A Fazer** do Kanban: *"Implementar busca e filtro de tarefas"*.
2. A funcionalidade foi implementada (método `buscar()` no repositório, parâmetros no endpoint `GET /api/tarefas` e controles na interface).
3. Novos testes automatizados foram adicionados em `tests/test_filtro.py`.
4. O card foi movido para **Concluído** após a implementação e os testes passarem no CI.

Essa mudança demonstra a **adaptabilidade e flexibilidade** das metodologias ágeis: o escopo evoluiu de forma controlada, documentada e versionada, sem comprometer o que já estava funcionando.

---

## 🧩 Diagramas UML

Os diagramas de modelagem do sistema estão em [`docs/`](docs/):

- **Diagrama de Casos de Uso** — `docs/diagrama_casos_de_uso.png`
- **Diagrama de Classes** — `docs/diagrama_classes.png`

---

## 🛠️ Tecnologias utilizadas

| Categoria | Ferramenta |
|-----------|------------|
| Linguagem | Python 3 |
| Framework web | Flask |
| Banco de dados | SQLite |
| Testes | PyTest |
| Integração Contínua | GitHub Actions |
| Gestão de tarefas | GitHub Projects (Kanban) |

---

## 👤 Autor

Projeto desenvolvido para a disciplina de **Engenharia de Software** — UniFECAF.
