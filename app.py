from flask import Flask, request, jsonify
import json
import csv
import os

app = Flask(__name__)

clientes = './csv/clientes.csv'
produtos = './csv/produtos.csv'
ordem = './csv/ordem.csv'

def id_cliente():
    if not os.path.exists(clientes):
        return 1
    with open(clientes, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) > 1:
            return int(lines[-1].split(",")[0]) + 1
        return 1
    
def id_produto():
    if not os.path.exists(produtos):
        return 1
    with open(produtos, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) > 1:
            return int(lines[-1].split(",")[0]) + 1
        return 1
    
def id_ordem():
    if not os.path.exists(ordem):
        return 1
    with open(ordem, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) > 1:
            return int(lines[-1].split(",")[0]) + 1
        return 1

# Criar arquivo CSV
if not os.path.exists(clientes):
    # Cria o arquivo CSV
    open(clientes, mode='w')
    cabecalho = [
        ['ID', 'Nome', 'Sobrenome', 'Nascimento', 'CPF']
    ]
    with open(clientes, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cabecalho)
else:
    print("O Arquivo ja existe!")

# Criar arquivo CSV
if not os.path.exists(produtos):
    # Cria o arquivo CSV
    open(produtos, mode='w')
    cabecalho = [
        ['ID', 'Nome', 'Fornecedor', 'Quantidade']
    ]
    with open(produtos, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cabecalho)
else:
    print("O Arquivo ja existe!")

# Criar arquivo CSV
if not os.path.exists(ordem):
    # Cria o arquivo CSV
    open(ordem, mode='w')
    cabecalho = [
        ['ID', 'ID_Cliente', 'ID_Produto']
    ]
    with open(ordem, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(cabecalho)
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
    id = id_cliente()
    data = [id, data_json.get("nome"), data_json.get("sobrenome"), data_json.get("nascimento"), data_json.get("cpf")]
    with open(clientes, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    return jsonify({"message": "Cliente adicionado com sucesso!"}), 200

# Atualizar clientes
@app.route("/att_clientes/<int:id>", methods=["PUT"])
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

# Exibir Informações dos Produtos
@app.route("/produtos", methods=["GET"])
def exebir_produtos():
    with open(produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        dados = [row for row in reader]
    return jsonify(dados)

# Adicionar novos clientes
@app.route("/add_produtos", methods=["POST"])
def add_produtos():
    data_json = request.get_json()
    id = id_produto()
    data = [id, data_json.get("nome"), data_json.get("fornecedor"), data_json.get("quantidade")]
    with open(produtos, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    return jsonify({"message": "Produto adicionado com sucesso!"}), 200

# Atualizar produtos
@app.route("/att_produtos/<int:id>", methods=["PUT"])
def atualizar_produtos(id):
    dados_json = request.get_json()
    rows = []

    with open(produtos, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        rows.append(cabecalho)

        for row in reader:
            if int(row[0]) == id:
                row[1] = dados_json.get("nome", row[1])
                row[2] = dados_json.get("fornecedor", row[2])
                row[3] = dados_json.get("quantidade", row[3])
            rows.append(row)

    with open(produtos, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return jsonify({"mensagem": "Produto atualizado com sucesso!"}), 200

# Excluir produto
@app.route("/del_produto/<int:id>", methods=["DELETE"])
def deletar_produto(id):
    with open(produtos, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        rows = [cabecalho]

        for row in reader:
            if row[0] != str(id):
                rows.append(row)
            else:
                print(f"ID {id} encontrado e removido.")

    with open(produtos, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return jsonify({"message": f"Produto com ID {id} excluído com sucesso."}), 200

# Exibir Informações dos ordem
@app.route("/ordem", methods=["GET"])
def exibir_ordem():
    with open(ordem, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        dados = [row for row in reader]
    return jsonify(dados)

# Adicionar novos ordem
@app.route("/add_ordem", methods=["POST"])
def add_ordem():
    data_json = request.get_json()
    id = id_ordem()
    data = [id, data_json.get("id_cliente"), data_json.get("id_produto")]
    with open(ordem, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    return jsonify({"message": "Ordem adicionado com sucesso!"}), 200

# Atualizar produtos
@app.route("/att_ordem/<int:id>", methods=["PUT"])
def atualizar_ordem(id):
    dados_json = request.get_json()
    rows = []

    with open(ordem, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        rows.append(cabecalho)

        for row in reader:
            if int(row[0]) == id:
                row[1] = dados_json.get("id_cliente", row[1])
                row[2] = dados_json.get("id_produto", row[2])
            rows.append(row)

    with open(ordem, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return jsonify({"mensagem": "Ordem atualizado com sucesso!"}), 200

# Excluir produto
@app.route("/del_ordem/<int:id>", methods=["DELETE"])
def deletar_ordem(id):
    with open(ordem, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        rows = [cabecalho]

        for row in reader:
            if row[0] != str(id):
                rows.append(row)
            else:
                print(f"ID {id} encontrado e removido.")

    with open(ordem, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return jsonify({"message": f"Ordem com ID {id} excluído com sucesso."}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

