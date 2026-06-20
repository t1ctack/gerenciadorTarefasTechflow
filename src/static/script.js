/*
  script.js
  ---------
  Logica do front-end: consome a API REST (/api/tarefas) e renderiza o quadro
  Kanban. Tudo e feito com fetch() nativo, sem bibliotecas externas.
*/

const API = "/api/tarefas";
const COLUNAS = ["a_fazer", "em_progresso", "concluido"];
const PROXIMO_STATUS = { a_fazer: "em_progresso", em_progresso: "concluido" };
const STATUS_ANTERIOR = { concluido: "em_progresso", em_progresso: "a_fazer" };

// Exibe uma mensagem temporaria de feedback ao usuario.
function mostrarMensagem(texto, tipo) {
  const el = document.getElementById("mensagem");
  el.textContent = texto;
  el.className = "mensagem " + (tipo || "");
  if (texto) setTimeout(() => { el.textContent = ""; el.className = "mensagem"; }, 3000);
}

// Monta os parametros de busca/filtro a partir dos campos da tela.
function montarQuery() {
  const params = new URLSearchParams();
  const busca = document.getElementById("busca").value.trim();
  const prioridade = document.getElementById("filtro-prioridade").value;
  if (busca) params.set("busca", busca);
  if (prioridade) params.set("prioridade", prioridade);
  const q = params.toString();
  return q ? "?" + q : "";
}

// Busca as tarefas na API e redesenha o quadro.
async function carregarTarefas() {
  try {
    const resp = await fetch(API + montarQuery());
    const tarefas = await resp.json();
    renderizar(tarefas);
  } catch (e) {
    mostrarMensagem("Erro ao carregar tarefas.", "erro");
  }
}

// Renderiza os cards nas colunas corretas do Kanban.
function renderizar(tarefas) {
  COLUNAS.forEach((status) => {
    const coluna = document.getElementById("col-" + status);
    coluna.innerHTML = "";
    const doStatus = tarefas.filter((t) => t.status === status);
    if (doStatus.length === 0) {
      coluna.innerHTML = '<p class="vazio">Nenhuma tarefa.</p>';
      return;
    }
    doStatus.forEach((t) => coluna.appendChild(criarCard(t)));
  });
}

// Cria o elemento HTML de um card de tarefa.
function criarCard(t) {
  const card = document.createElement("div");
  card.className = "card " + t.prioridade;

  const titulo = document.createElement("h4");
  titulo.textContent = t.titulo;
  card.appendChild(titulo);

  if (t.descricao) {
    const desc = document.createElement("p");
    desc.textContent = t.descricao;
    card.appendChild(desc);
  }

  const tag = document.createElement("span");
  tag.className = "tag";
  tag.textContent = "Prioridade: " + t.prioridade;
  card.appendChild(tag);

  const acoes = document.createElement("div");
  acoes.className = "acoes";

  if (STATUS_ANTERIOR[t.status]) {
    acoes.appendChild(botao("<", () => mover(t, STATUS_ANTERIOR[t.status])));
  }
  if (PROXIMO_STATUS[t.status]) {
    acoes.appendChild(botao("Avancar >", () => mover(t, PROXIMO_STATUS[t.status])));
  }
  const excluir = botao("Excluir", () => removerTarefa(t.id));
  excluir.className = "excluir";
  acoes.appendChild(excluir);

  card.appendChild(acoes);
  return card;
}

function botao(texto, aoClicar) {
  const b = document.createElement("button");
  b.textContent = texto;
  b.onclick = aoClicar;
  return b;
}

// Cria uma nova tarefa via POST.
async function criarTarefa() {
  const titulo = document.getElementById("titulo").value.trim();
  const descricao = document.getElementById("descricao").value.trim();
  const prioridade = document.getElementById("prioridade").value;
  if (!titulo) { mostrarMensagem("Informe um titulo.", "erro"); return; }

  try {
    const resp = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ titulo, descricao, prioridade }),
    });
    const dados = await resp.json();
    if (resp.ok) {
      document.getElementById("titulo").value = "";
      document.getElementById("descricao").value = "";
      mostrarMensagem("Tarefa adicionada!", "sucesso");
      carregarTarefas();
    } else {
      mostrarMensagem(dados.erro || "Erro ao criar tarefa.", "erro");
    }
  } catch (e) {
    mostrarMensagem("Erro de conexao.", "erro");
  }
}

// Move a tarefa para outro status (coluna) via PUT.
async function mover(tarefa, novoStatus) {
  await fetch(API + "/" + tarefa.id, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status: novoStatus }),
  });
  carregarTarefas();
}

// Remove a tarefa via DELETE.
async function removerTarefa(id) {
  if (!confirm("Deseja realmente excluir esta tarefa?")) return;
  await fetch(API + "/" + id, { method: "DELETE" });
  mostrarMensagem("Tarefa removida.", "sucesso");
  carregarTarefas();
}

// Liga os eventos da tela.
document.getElementById("btn-criar").onclick = criarTarefa;
document.getElementById("busca").oninput = carregarTarefas;
document.getElementById("filtro-prioridade").onchange = carregarTarefas;
document.getElementById("btn-limpar").onclick = () => {
  document.getElementById("busca").value = "";
  document.getElementById("filtro-prioridade").value = "";
  carregarTarefas();
};

// Carrega as tarefas ao abrir a pagina.
carregarTarefas();
