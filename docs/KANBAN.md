# 📋 Quadro Kanban — GitHub Projects

Este documento registra o planejamento de tarefas do projeto. No **GitHub Projects**, estes itens devem ser criados como *cards* nas colunas **To Do (A Fazer)**, **In Progress (Em Progresso)** e **Done (Concluído)**.

> ℹ️ O quadro Kanban oficial deve ser montado na aba **Projects** do repositório no GitHub (instruções no final). Abaixo está o conteúdo de referência, com **12 cards**.

## ✅ Done (Concluído)

1. Configurar estrutura inicial do repositório
2. Escrever README com objetivo, escopo e metodologia
3. Implementar modelo de Tarefa e repositório (SQLite)
4. Implementar validação de entradas
5. Criar API REST (CRUD) com Flask
6. Desenvolver interface web estilo Kanban
7. Escrever testes unitários (validação e repositório)
8. Escrever testes de integração da API
9. Configurar pipeline de CI com GitHub Actions
10. Criar diagramas UML e documentação

## 🚧 In Progress (Em Progresso)

11. Implementar busca e filtro de tarefas *(mudança de escopo)*

## 🗒️ To Do (A Fazer)

12. Adicionar autenticação de usuários (melhoria futura)

---

## Mapa: cards → commits

| # | Card | Commit relacionado |
|---|------|--------------------|
| 1 | Estrutura inicial | `chore: estrutura inicial e configuração do projeto` |
| 2 | README | `docs: adiciona README com objetivo, escopo e metodologia` |
| 3 | Modelo + repositório | `feat: implementa modelo de Tarefa e repositório SQLite` |
| 4 | Validação | `feat: adiciona validação de entradas de tarefas` |
| 5 | API REST | `feat: cria API REST CRUD com Flask` |
| 6 | Interface | `feat: adiciona interface web estilo Kanban` |
| 7 | Testes unitários | `test: adiciona testes de validação e repositório` |
| 8 | Testes de API | `test: adiciona testes de integração da API` |
| 9 | CI | `ci: configura pipeline de CI com GitHub Actions` |
| 10 | UML/docs | `docs: adiciona diagramas UML e documentação do Kanban` |
| 11 | Busca/filtro | `feat: adiciona busca e filtro de tarefas (mudança de escopo)` |
| 12 | Justificativa | `docs: registra justificativa da mudança de escopo no README` |

---

## 🧭 Como montar o quadro no GitHub Projects

1. No repositório, clique na aba **Projects** → **New project** → modelo **Board**.
2. Crie/renomeie as três colunas: **To Do**, **In Progress**, **Done**.
3. Para cada item acima, clique em **+ Add item** na coluna correspondente e digite o texto do card.
4. (Opcional) Vincule cada card a um commit ou issue usando o `#`.
