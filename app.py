from flask import Flask, render_template, abort
from urllib.parse import quote

app = Flask(__name__)

# Edite preços, descrições e o WhatsApp (55 + DDD + número, só dígitos) de cada vendedor.
CADEIRAS = [
    {
        "slug": "escolar-verde-menta",
        "nome": "Cadeira escolar verde-menta",
        "preco": 120.00,
        "estado": "Usada, com desgaste nas bordas",
        "descricao": "Assento e encosto em laminado verde-menta sobre estrutura de tubo preto. "
                     "Clássico de sala de aula, firme e leve. Tem pequenos arranhões no assento "
                     "e lascas na borda do encosto.",
        "fotos": ["img/verde1.jpg", "img/verde2.jpg"],
        "vendedor": {"nome": "Nicollas Augusto", "whatsapp": "5500000000000"},
    },
    {
        "slug": "giratoria-azul",
        "nome": "Cadeira giratória azul com braços",
        "preco": 250.00,
        "estado": "Usada, bom estado",
        "descricao": "Cadeira de escritório giratória com rodízios, braços reguláveis e estofado "
                     "azul. Base de cinco pontas. Estofado com leves marcas de uso.",
        "fotos": ["img/azul1.jpg", "img/azul2.jpg"],
        "vendedor": {"nome": "Roger Clemente", "whatsapp": "5500000000000"},
    },
    {
        "slug": "fixa-preta-estofada",
        "nome": "Cadeira fixa preta estofada",
        "preco": 90.00,
        "estado": "Usada, assento com rasgos",
        "descricao": "Cadeira fixa com estrutura de aço preta, assento e encosto estofados em "
                     "courino. Ótima para recepção ou estudo. O assento tem rasgos no courino "
                     "e vai precisar de reforma.",
        "fotos": ["img/preta1.jpg", "img/preta2.jpg"],
        "vendedor": {"nome": "Nicolas Moreira", "whatsapp": "5500000000000"},
    },
    {
        "slug": "plastica-preta-perfurada",
        "nome": "Cadeira preta de polipropileno",
        "preco": 110.00,
        "estado": "Usada, bom estado",
        "descricao": "Cadeira empilhável com assento e encosto em plástico preto, encosto perfurado "
                     "e estrutura de aço tipo trenó. Boa para auditório, reunião ou mesa de desenho.",
        "fotos": ["img/plastica1.jpg", "img/plastica2.jpg"],
        "vendedor": {"nome": "Iago Braga", "whatsapp": "5500000000000"},
    },
    {
        "slug": "escolar-cinza-azulada",
        "nome": "Cadeira escolar cinza-azulada",
        "preco": 80.00,
        "estado": "Usada, bom estado",
        "descricao": "Cadeira com assento e encosto em plástico cinza-azulado e estrutura de tubo "
                     "cinza-claro, com ponteiras nos pés. Leve, resistente e fácil de limpar.",
        "fotos": ["img/escolar1.jpg", "img/escolar2.jpg"],
        "vendedor": {"nome": "Iago Braga", "whatsapp": "5500000000000"},
    },
    {
        "slug": "giratoria-preta-baixa",
        "nome": "Cadeira giratória preta com base cromada",
        "preco": 140.00,
        "estado": "Usada, bom estado",
        "descricao": "Cadeira de escritório sem braços, com regulagem de altura, rodízios e base "
                     "cromada de cinco pontas. Estofado em courino preto.",
        "fotos": ["img/swivel1.jpg", "img/swivel2.jpg"],
        "vendedor": {"nome": "Iago Braga", "whatsapp": "5500000000000"},
    },
    {
        "slug": "estofada-preta-listrada",
        "nome": "Cadeira estofada preta com pés cinza",
        "preco": 100.00,
        "estado": "Usada, bom estado",
        "descricao": "Cadeira fixa com assento e encosto estofados em courino preto com costuras "
                     "verticais e estrutura de aço. Boa para recepção, escritório ou estudo.",
        "fotos": ["img/estofada1.jpg", "img/estofada2.jpg"],
        "vendedor": {"nome": "Iago Braga", "whatsapp": "5500000000000"},
    },
]


def brl(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


app.jinja_env.filters["brl"] = brl


@app.route("/")
def index():
    return render_template("index.html", cadeiras=CADEIRAS)


@app.route("/cadeira/<slug>")
def cadeira(slug):
    c = next((x for x in CADEIRAS if x["slug"] == slug), None)
    if not c:
        abort(404)
    msg = quote(f"Olá {c['vendedor']['nome']}, tenho interesse na {c['nome']} ({brl(c['preco'])}).")
    link = f"https://wa.me/{c['vendedor']['whatsapp']}?text={msg}"
    return render_template("cadeira.html", c=c, link=link)


@app.errorhandler(404)
def nao_achou(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
