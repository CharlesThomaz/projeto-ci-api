from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração do MySQL (igual ao que está no docker-compose)
app.config['MYSQL_HOST'] = 'db'           # nome do serviço no docker-compose
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskdb'

mysql = MySQL(app)

@app.route('/')
def index():
    return 'API conectada ao MySQL!'

@app.route('/items', methods=['GET'])
def get_items():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM items')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    # Pega os dados enviados no corpo da requisição
    item_data = request.get_json()
    
    # Verifica se os dados necessários estão presentes
    if not item_data or 'nome' not in item_data:
        return jsonify({'error': 'Nome do item é obrigatório'}), 400

    
    nome = item_data['nome']

    # Adiciona o item ao banco de dados
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO items (nome) VALUES (%s)', (nome,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Item adicionado com sucesso'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
