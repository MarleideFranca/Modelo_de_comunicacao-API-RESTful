import requests

# URL do servidor REST
url = 'http://127.0.0.1:5000/api/users'

# Fazendo uma requisição GET à API
response = requests.get(url)

# Verificando o status da resposta
if response.status_code == 200:
    # Exibindo os dados retornados
    users = response.json()
    print("Usuários recebidos da API:")
    for user in users:
        print(f"ID: {user['id']}, Nome: {user['name']}")
else:
    print("Erro ao acessar a API")




