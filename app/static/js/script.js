const botaoMenu = document.getElementById("menu-toggle");
const links = document.getElementById("nav-links");

if (botaoMenu && links) {
  botaoMenu.addEventListener("click", () => {
    links.classList.toggle("aberto");
  });
}

async function atualizarStatus() {
  const alvo = document.getElementById("status-servidor");
  if (!alvo) return;

  try {
    const resposta = await fetch("/api/status");
    const dados = await resposta.json();
    alvo.textContent = `servidor: ${dados.status} · ambiente: ${dados.ambiente} · ${dados.hora_servidor}`;
  } catch (erro) {
    alvo.textContent = "não foi possível contatar o servidor.";
  }
}

atualizarStatus();
setInterval(atualizarStatus, 5000);
