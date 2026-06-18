# Roteiro do Vídeo Pitch (até 4 minutos)

> **Como usar:** este é um roteiro-guia. Fale com naturalidade, no seu ritmo, olhando
> para a câmera ou narrando enquanto compartilha a tela. Os tempos são apenas uma
> sugestão para você caber nos 4 minutos. Grave com a tela do projeto aberta
> (VS Code, navegador com o sistema rodando e o GitHub) para mostrar tudo ao vivo.

---

## 0:00 – 0:30 | Abertura e apresentação do projeto

> "Olá! Meu nome é [SEU NOME] e neste vídeo vou apresentar o projeto **Gerenciador de
> Tarefas TechFlow**, desenvolvido para a disciplina de Engenharia de Software.
>
> O cenário é o seguinte: a TechFlow Solutions foi contratada por uma startup de
> logística que precisava de um sistema ágil para acompanhar o fluxo de trabalho da
> equipe em tempo real, priorizar tarefas críticas e organizar as entregas. A solução
> que desenvolvi é um sistema web de gerenciamento de tarefas no estilo **Kanban**."

*(Mostre na tela: o sistema aberto no navegador com as três colunas.)*

---

## 0:30 – 1:10 | Metodologia ágil e organização do Kanban

> "A metodologia ágil escolhida foi o **Kanban**, ideal para fluxo contínuo de trabalho.
> Toda a gestão do projeto foi feita no **GitHub Projects**, com um quadro dividido em
> três colunas: *A Fazer (To Do)*, *Em Progresso (In Progress)* e *Concluído (Done)*.
>
> Cada tarefa do desenvolvimento virou um card, e cada card está ligado a um commit
> real no repositório — então dá para rastrear exatamente o que foi feito e quando."

*(Mostre na tela: a aba Projects do GitHub com os cards distribuídos nas colunas.)*

---

## 1:10 – 2:00 | Demonstração do sistema rodando

> "Vamos ver o sistema funcionando. Aqui eu posso **criar** uma nova tarefa, definindo
> título, descrição, status e prioridade."

*(Crie uma tarefa ao vivo.)*

> "A tarefa aparece imediatamente na coluna correspondente. Posso **mover** a tarefa
> entre as colunas, **editar** os dados e **excluir** quando concluída — ou seja, o
> sistema implementa o CRUD completo: criar, ler, atualizar e deletar.
>
> O back-end foi feito em **Python com Flask**, expondo uma API REST, e os dados são
> salvos num banco **SQLite**. O front-end consome essa API com JavaScript puro."

*(Mostre: mover um card, editar e excluir uma tarefa.)*

---

## 2:00 – 2:40 | Testes automatizados

> "Qualidade de software foi um ponto central. O projeto tem **29 testes automatizados**
> escritos com **PyTest**, organizados por responsabilidade: testes de validação de
> entradas, testes do CRUD na camada de dados, testes de integração da API e testes da
> funcionalidade de busca e filtro.
>
> Rodando `pytest` no terminal, todos os 29 testes passam. Isso garante que qualquer
> alteração futura não quebre o que já funciona."

*(Mostre na tela: rodar `pytest` no terminal e os testes passando em verde.)*

---

## 2:40 – 3:10 | GitHub Actions (Integração Contínua)

> "Para automatizar esse controle de qualidade, configurei um pipeline de **Integração
> Contínua com GitHub Actions**. A cada push, o GitHub automaticamente instala as
> dependências, faz a verificação de qualidade do código com o flake8 e roda toda a
> suíte de testes.
>
> Aqui na aba Actions dá para ver a execução concluída com o check verde — ou seja, o
> código está sempre validado."

*(Mostre na tela: a aba Actions do GitHub com o workflow concluído em verde.)*

---

## 3:10 – 3:40 | Mudança de escopo

> "Durante o projeto, simulei uma **mudança de escopo**, que é algo comum em projetos
> ágeis reais. A startup percebeu que, com muitas tarefas, ficava difícil localizar uma
> tarefa específica. Então adicionei uma funcionalidade de **busca por texto e filtro
> por prioridade**.
>
> Essa mudança foi gerenciada do jeito certo: criei um novo card no Kanban, fiz um
> commit específico implementando a feature, escrevi novos testes para ela e documentei
> a justificativa no README. Isso mostra como o versionamento e o Kanban ajudam a
> absorver mudanças sem perder o controle do projeto."

*(Mostre na tela: a barra de busca/filtro funcionando e o commit da mudança.)*

---

## 3:40 – 4:00 | Reflexão final

> "Para encerrar: este projeto me mostrou na prática como a Engenharia de Software vai
> muito além de escrever código. Planejamento com metodologia ágil, modelagem com
> diagramas UML, versionamento com Git, testes automatizados e integração contínua são
> o que diferenciam um software amador de um produto confiável no mercado de tecnologia.
>
> Essas práticas reduzem falhas, facilitam a colaboração em equipe e tornam o software
> sustentável a longo prazo. Obrigado por assistir!"

---

## Checklist técnico antes de gravar

- [ ] Sistema rodando localmente (`python -m flask --app src/app run` ou via `run.py`)
- [ ] Navegador aberto com o Kanban visível
- [ ] Terminal pronto para rodar `pytest`
- [ ] GitHub aberto em três abas: **Code**, **Projects** (Kanban) e **Actions**
- [ ] Microfone testado, tela limpa, notificações desativadas
- [ ] Gravação de no máximo 4 minutos
- [ ] Subir no YouTube (não listado) ou Google Drive e **deixar o link público**

> **Dica:** se travar na fala, regrave só o trecho. Não precisa ser perfeito — precisa
> ser claro e mostrar que **você** entende o que construiu.
