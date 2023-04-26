from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Odisseia',
        'autor': 'Homero'
    },
    {
        'id': 2,
        'titulo': 'A cabana do Pai Tomás',
        'autor': 'Harriet Beecher Stowe'
    },
    {
        'id': 3,
        'titulo': 'Frankenstein',
        'autor': 'Mary Shelley'
    },
]

# Consultar todos


@app.route('/livros', methods=['GET'])
def getLivros():
    return jsonify(livros)

# Obter livros por id


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# Editar livro por Id
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar


@app.route('/livros', methods=['POST'])
def inserir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro)

# Excluir um livro


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


# start server
app.run(port=5000, host='localhost', debug=True)
