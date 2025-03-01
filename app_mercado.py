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
@app.route("/clientes", methods=["GET"])
def cliente():
    with open(clientes, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        dados = [row for row in reader]
    return jsonify(dados)

# Adicionar novos clientes
@app.route("/add_clientes", methods=["POST"])
def add_cliente():
    data_json = request.get_json()
    id = gerar_id()
    data = [id] + [data_json.get("nome"), data_json.get("sobrenome"), data_json.get("nascimento"), data_json.get("cpf")]
    with open(clientes, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    return jsonify({"message": "Cliente adicionado com sucesso!"}), 200

# Atualizar clientes
@app.route("/atualizar_clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    dados_json = request.get_json()
    rows = []

    with open(clientes, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        rows.append(cabecalho)

        for row in reader:
            if int(row[0]) == id:
                row[1] = dados_json.get("nome", row[1])
                row[2] = dados_json.get("sobrenome", row[2])
                row[3] = dados_json.get("nascimento", row[3])
                row[4] = dados_json.get("cpf", row[4])
            rows.append(row)

    with open(clientes, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return jsonify({"mensagem": "Cliente atualizado com sucesso!"}), 200

# Excluir cliente
@app.route("/del_clientes/<int:id>", methods=["DELETE"])
def deletar_cliente(id):
    with open(clientes, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        rows = [cabecalho]

        for row in reader:
            if row[0] != str(id):
                rows.append(row)
            else:
                print(f"ID {id} encontrado e removido.")

    with open(clientes, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return jsonify({"message": f"Cliente com ID {id} excluído com sucesso."}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

