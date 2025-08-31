#Servidor de API (Servidor REST)
#Este servidor irá expor um endpoint simples que retorna uma lista de usuários.

from flask import Flask, jsonify,request
app = Flask(__name__)

# Lista simulada de usuários
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Rota inicial
@app.route('/')
def home():
    return "Bem-vindo à API!"

# Rota para obter todos os usuários
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Rota para adicionar um novo usuário (POST)
@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if not new_user or "name" not in new_user:
        return jsonify({"error": "Nome do usuário é obrigatório"}), 400
    
    new_id = max(user["id"] for user in users) + 1 if users else 1
    user = {"id": new_id, "name": new_user["name"]}
    users.append(user)
    return jsonify(user), 201

# Rota para atualizar um usuário existente (PUT)
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_data.get("name", user["name"])
            return jsonify(user)
    return jsonify({"error": "Usuário não encontrado"}), 404

# Rota para deletar um usuário (DELETE)
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "Usuário removido com sucesso"})
    return jsonify({"error": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


















  

