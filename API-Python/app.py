from flask import Flask, jsonify, request

# Crio uma api com o nome da pasta atual
app = Flask(__name__)

# Crio uma lista de filmes
livros = [
    {
        'id': 1,
        'title': 'O Senhor dos Anéis - A Sociedade do Anel',
        'author': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'title': 'Harry Potter e a Pedra Filosofal',
        'author': 'J.K Howling'
    },
    {
        'id': 3,
        'title': 'Hábitos Atômicos',
        'author': 'James Clear'
    },
]


@app.route('/livros', methods=['GET'])
def get_books():
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['GET'])
def get_book(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


@app.route('/livros/<int:id>', methods=['PUT'])
def update_book(id):
    # recebo as alterações do corpo da requisição
    updated_book = request.get_json()
    # percorro todos os livros até achar o q quero editar
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            # atualizo o livro
            livros[indice].update(updated_book)
            # retorno o livro que foi editado
            return jsonify(livros[indice])


@app.route('/livros', methods=['POST'])
def create_book():
    new_book = request.get_json()
    livros.append(new_book)

    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_book(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
