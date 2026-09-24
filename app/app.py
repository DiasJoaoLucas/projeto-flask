from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

MENU = [
    {"nome": "Início", "rota": "/", "endpoint": "home"},
    {"nome": "Sobre", "rota": "/sobre", "endpoint": "sobre"},
    {"nome": "Projetos", "rota": "/projetos", "endpoint": "projetos"},
    {"nome": "Contato", "rota": "/contato", "endpoint": "contato"},
]


@app.context_processor
def injetar_globais():
    return dict(menu=MENU, ano_atual=datetime.now().year)


@app.route("/")
def home():
    return render_template("index.html", titulo="Início", ativo="home")


@app.route("/sobre")
def sobre():
    integrantes = [
        {"nome": "Alefe Ruan", "papel": "Desenvolvimento"},
        {"nome": "Clara Fiuza Serejo", "papel": "Desenvolvimento"},
        {"nome": "João Lucas Dias", "papel": "Infraestrutura / Docker"},
    ]
    return render_template(
        "sobre.html", titulo="Sobre", ativo="sobre", integrantes=integrantes
    )


@app.route("/projetos")
def projetos():
    lista_projetos = [
        {
            "nome": "App Flask em Docker",
            "descricao": "Aplicação web conteinerizada com Docker, usada neste trabalho.",
            "status": "Concluído",
        },
        {
            "nome": "Monitoramento de containers",
            "descricao": "Ideia de expansão: painel simples de status dos containers.",
            "status": "Planejado",
        },
        {
            "nome": "API de segurança",
            "descricao": "Rota /api/status simulando um endpoint de verificação de saúde.",
            "status": "Em andamento",
        },
    ]
    return render_template(
        "projetos.html", titulo="Projetos", ativo="projetos", projetos=lista_projetos
    )


@app.route("/contato")
def contato():
    return render_template("contato.html", titulo="Contato", ativo="contato")


@app.route("/api/status")
def api_status():
    return jsonify(
        {
            "status": "ok",
            "aplicacao": "projeto-flask",
            "ambiente": "docker",
            "hora_servidor": datetime.now().strftime("%H:%M:%S"),
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
