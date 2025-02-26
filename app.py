from flask import Flask, request, jsonify
import json
import csv
import os

app = Flask(__name__)

def gerar_id():
    if not os.path.exists(clientes):
        return 1
    with open(clientes, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) > 1:
            return int(lines[-1].split(",")[0]) + 1
        return 1

clientes = './csv/clientes.csv'
produtos = './csv/produtos.csv'
ordem = './csv/ordem.csv'

# Criar arquivo CSV
if not os.path.exists(clientes):
    # Cria o arquivo CSV
    open(clientes, mode='w')
    cabecalho = [
        ['Nome', 'Sobrenome', 'Nascimento', 'CPF']
    ]
    with open(clientes, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cabecalho)
else:
    print("O Arquivo ja existe!")

if not os.path.exists(ordem):
    # Cria o arquivo CSV
    open(ordem, mode='w').close()
else:
    print("O Arquivo ja existe!")

# Exibir Informações dos Clientes
@app.route("/cliente", methods=["GET"])
def cliente():
    with open(clientes, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        dados = [row for row in reader]
    return jsonify(dados)

# Adicionar informações nos arquivos CSV
@app.route("/add_cliente", methods=["POST"])
def add_cliente():
    data_json = request.get_json()
    id = gerar_id()
    data = [id] + [data_json.get("nome"), data_json.get("sobrenome"), data_json.get("nascimento"), data_json.get("cpf")]
    with open(clientes, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    return jsonify({"message": "Cliente adicionado com sucesso!"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

