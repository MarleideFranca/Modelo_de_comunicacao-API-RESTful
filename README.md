# 🏗 Modelo de Comunicação por API RESTful

Este projeto apresenta um **modelo de comunicação utilizando API RESTful**, implementado em Python com Flask. Ele demonstra como clientes e servidores podem interagir usando requisições HTTP para operações CRUD (Create, Read, Update, Delete).

---

## 📦 Funcionalidades

* Obter todos os usuários (`GET /api/users`)
* Adicionar um novo usuário (`POST /api/users`)
* Atualizar um usuário existente (`PUT /api/users/<id>`)
* Remover um usuário (`DELETE /api/users/<id>`)

---

## ⚙️ Pré-requisitos

* Python 3.10 ou superior
* Flask instalado:

```bash
pip install flask
```

---

## 🚀 Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/MarleideFranca/Modelo_de_comunicacao-API-RESTful.git
cd Modelo_de_comunicacao-API-RESTful
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python app.py
```

4. Acesse a API em: `http://127.0.0.1:5000/api/users`

---

## 🔧 Exemplos de uso

### 1️⃣ Listar todos os usuários (GET)

**Curl:**

```bash
curl -X GET http://127.0.0.1:5000/api/users
```

### 2️⃣ Adicionar um usuário (POST)

**Curl:**

```bash
curl -X POST http://127.0.0.1:5000/api/users \
-H "Content-Type: application/json" \
-d '{"name": "Diana}'
```
---

### 3️⃣ Atualizar um usuário (PUT)

**Curl:**

```bash
curl -X PUT http://127.0.0.1:5000/api/users/2 \
-H "Content-Type: application/json" \
-d '{"name": "Luciano"}'
```
---

### 4️⃣ Remover um usuário (DELETE)

**Curl:**

```bash
curl -X DELETE http://127.0.0.1:5000/api/users/1
```
## 🔄 Comunicação

### Síncrona

* **Definição:** O cliente envia uma requisição e espera a resposta antes de continuar.
* **Exemplo:** `GET /api/users` bloqueia até receber os dados.

### Assíncrona

* **Definição:** O cliente envia a requisição e continua a execução sem esperar a resposta.
* **Exemplo:** Não implementado neste projeto, mas poderia ser feito com:

  * `AJAX` ou `fetch` com Promises
  * Filas de mensagens (RabbitMQ, Kafka)

---

## ⚖️ Comparação: Síncrono vs Assíncrono

| Aspecto            | Síncrono                    | Assíncrono                                                      |
| ------------------ | --------------------------- | --------------------------------------------------------------- |
| Espera da resposta | Sim, bloqueia o cliente     | Não, cliente continua a execução                                |
| Complexidade       | Baixa                       | Média/Alta, exige callbacks/promises ou filas                   |
| Performance        | Limitada se houver espera   | Melhor para cargas altas ou tarefas longas                      |
| Uso comum          | Operações rápidas e simples | Processamento pesado, notificações em tempo real, microserviços |

---

## 💡 Quando usar comunicação assíncrona

* Processamento de **tarefas longas** sem bloquear o cliente
* **Notificações em tempo real** (chat, alertas, dashboards)
* Sistemas com **alta concorrência**
* Integração com **microserviços**

---

🛠 Tecnologias Utilizadas

Python 3.10+

Flask

Git

GitHub

Postman (para testes de API)

cURL (para testes de linha de comando)

## 📚 Referências

* [RESTful API Design](https://restfulapi.net/)
* [Flask Documentation](https://flask.palletsprojects.com/)

