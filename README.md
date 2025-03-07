---

Este manual explica como utilizar a API de Supermercado para gerenciar clientes, produtos e ordens de venda. A API foi construída com o framework Flask e utiliza arquivos CSV para persistência de dados. Todas as requisições serão exemplificadas usando o **Postman**, uma ferramenta popular para testar APIs.

**Pré-requisitos**

1. **Servidor Rodando**: Certifique-se de que o código Python da API está em execução. Execute o comando abaixo no terminal, na pasta onde o arquivo Python está salvo:bashO servidor iniciará em http://0.0.0.0:5000 por padrão (ou http://localhost:5000 localmente).
    
    ```bash
    python nome_do_arquivo.py
    ```
    
2. **Postman Instalado**: Baixe e instale o Postman (disponível em [postman.com](https://www.postman.com/)) para testar as requisições.
3. **Estrutura de Pastas**: Certifique-se de que a pasta csv/ existe no mesmo diretório do arquivo Python e que os arquivos clientes.csv, produtos.csv e ordem.csv foram criados (eles são gerados automaticamente na primeira execução).

---

**Estrutura Geral da API**

A API possui três entidades principais:

- **Clientes**: Informações sobre os clientes do supermercado.
- **Produtos**: Dados dos produtos disponíveis.
- **Ordens**: Registro das vendas (associa clientes a produtos).

Cada entidade suporta as operações **CRUD** (Create, Read, Update, Delete) via métodos HTTP:

- **GET**: Listar dados.
- **POST**: Adicionar novos dados.
- **PUT**: Atualizar dados existentes.
- **DELETE**: Excluir dados.

Os dados são enviados e recebidos no formato **JSON**, exceto na leitura (GET), que retorna uma lista de arrays.

---

**Como Fazer Requisições no Postman**

**Configurações Básicas no Postman**

1. Abra o Postman e crie uma nova requisição clicando em **"New" > "HTTP Request"**.
2. Escolha o **método HTTP** (GET, POST, PUT, DELETE) no menu suspenso ao lado da URL.
3. Insira a **URL base**: http://localhost:5000 (ou o IP do servidor, se estiver hospedado remotamente).
4. Configure os parâmetros conforme necessário (query ou body, explicados abaixo).

---

**1. Rotas de Clientes**

**1.1. Listar Todos os Clientes**

- **Método**: GET
- **URL**: http://localhost:5000/clientes
- **Parâmetros**: Nenhum
- **Como Fazer**:
    1. No Postman, selecione **GET**.
    2. Digite a URL: http://localhost:5000/clientes.
    3. Clique em **Send**.
- **Resposta Esperada** (exemplo):json
    
    ```json
    [
      ["ID", "Nome", "Sobrenome", "Nascimento", "CPF"],
      ["1", "João", "Silva", "1990-05-15", "123.456.789-00"],
      ["2", "Maria", "Souza", "1985-10-20", "987.654.321-00"]
    ]
    ```
    

**1.2. Adicionar um Cliente**

- **Método**: POST
- **URL**: http://localhost:5000/add_clientes
- **Parâmetros**: Body (JSON)
- **Como Fazer**:
    1. No Postman, selecione **POST**.
    2. Digite a URL: http://localhost:5000/add_clientes.
    3. Vá para a aba **Body**, selecione **raw** e escolha **JSON** no menu suspenso.
    4. Insira os dados do cliente no formato abaixo:json
        
        ```json
        {
          "nome": "Ana",
          "sobrenome": "Pereira",
          "nascimento": "1995-03-10",
          "cpf": "111.222.333-44"
        }
        ```
        
    5. Clique em **Send**.
- **Resposta Esperada**:json
    
    ```json
    {
      "message": "Cliente adicionado com sucesso!"
    }
    ```
    
- **Nota**: O campo ID é gerado automaticamente pela API.

**1.3. Atualizar um Cliente**

- **Método**: PUT
- **URL**: http://localhost:5000/att_clientes/<id>
- **Parâmetros**:
    - Query: <id> na URL (ID do cliente a ser atualizado).
    - Body: JSON com os campos a atualizar (opcional).
- **Como Fazer**:
    1. No Postman, selecione **PUT**.
    2. Digite a URL com o ID, por exemplo: http://localhost:5000/att_clientes/1.
    3. Na aba **Body**, selecione **raw** e **JSON**, e insira os dados a atualizar:json
        
        ```json
        {
          "nome": "João Pedro",
          "cpf": "999.888.777-66"
        }
        ```
        
    4. Clique em **Send**.
- **Resposta Esperada**:json
    
    ```json
    {
      "mensagem": "Cliente atualizado com sucesso!"
    }
    ```
    
- **Nota**: Apenas os campos enviados no JSON serão atualizados.

**1.4. Excluir um Cliente**

- **Método**: DELETE
- **URL**: http://localhost:5000/del_clientes/<id>
- **Parâmetros**: Query (<id> na URL)
- **Como Fazer**:
    1. No Postman, selecione **DELETE**.
    2. Digite a URL com o ID, por exemplo: http://localhost:5000/del_clientes/1.
    3. Clique em **Send**.
- **Resposta Esperada**:json
    
    ```json
    {
      "message": "Cliente com ID 1 excluído com sucesso."
    }
    ```
    

---

**2. Rotas de Produtos**

**2.1. Listar Todos os Produtos**

- **Método**: GET
- **URL**: http://localhost:5000/produtos
- **Parâmetros**: Nenhum
- **Exemplo de Resposta**:json
    
    ```json
    [
      ["ID", "Nome", "Fornecedor", "Quantidade"],
      ["1", "Arroz", "Fornecedor A", "100"],
      ["2", "Feijão", "Fornecedor B", "50"]
    ]
    ```
    

**2.2. Adicionar um Produto**

- **Método**: POST
- **URL**: http://localhost:5000/add_produtos
- **Parâmetros**: Body (JSON)
- **Exemplo de Body**:json
    
    ```json
    {
      "nome": "Macarrão",
      "fornecedor": "Fornecedor C",
      "quantidade": "200"
    }
    ```
    

**2.3. Atualizar um Produto**

- **Método**: PUT
- **URL**: http://localhost:5000/att_produtos/<id>
- **Exemplo**: http://localhost:5000/att_produtos/1
- **Body (JSON)**:json
    
    ```json
    {
      "quantidade": "150"
    }
    ```
    

**2.4. Excluir um Produto**

- **Método**: DELETE
- **URL**: http://localhost:5000/del_produtos/<id>
- **Exemplo**: http://localhost:5000/del_produtos/1

---

**3. Rotas de Ordens**

**3.1. Listar Todas as Ordens**

- **Método**: GET
- **URL**: http://localhost:5000/ordem
- **Exemplo de Resposta**:json
    
    ```json
    [
      ["ID", "ID_Cliente", "ID_Produto"],
      ["1", "1", "2"],
      ["2", "2", "1"]
    ]
    ```
    

**3.2. Adicionar uma Ordem**

- **Método**: POST
- **URL**: http://localhost:5000/add_ordem
- **Body (JSON)**:json
    
    ```json
    {
      "id_cliente": "1",
      "id_produto": "2"
    }
    ```
    

**3.3. Atualizar uma Ordem**

- **Método**: PUT
- **URL**: http://localhost:5000/att_ordem/<id>
- **Exemplo**: http://localhost:5000/att_ordem/1
- **Body (JSON)**:json
    
    ```json
    {
      "id_produto": "3"
    }
    ```
    

**3.4. Excluir uma Ordem**

- **Método**: DELETE
- **URL**: http://localhost:5000/del_ordem/<id>
- **Exemplo**: http://localhost:5000/del_ordem/1

---

**Dicas Práticas**

1. **Parâmetros**:
    - **Query**: Usado nas URLs para especificar IDs (ex.: /del_clientes/1).
    - **Body**: Usado em POST e PUT para enviar dados no formato JSON.
2. **Teste Incremental**: Comece listando os dados (GET) para verificar o estado atual antes de adicionar, atualizar ou excluir.
3. **Erros**: Se algo der errado (ex.: arquivo CSV não encontrado), o Flask exibirá uma mensagem de erro no terminal onde o servidor está rodando.

---

**Exemplo Completo no Postman**

**Adicionar um Cliente e Associar a uma Ordem**

1. **POST** http://localhost:5000/add_clientes:json
    
    ```json
    {
      "nome": "Carlos",
      "sobrenome": "Mendes",
      "nascimento": "1980-07-25",
      "cpf": "555.666.777-88"
    }
    ```
    
2. **POST** http://localhost:5000/add_produtos:json
    
    ```json
    {
      "nome": "Leite",
      "fornecedor": "Fornecedor D",
      "quantidade": "300"
    }
    ```
    
3. **POST** http://localhost:5000/add_ordem:json
    
    ```json
    {
      "id_cliente": "3",  // ID gerado para Carlos
      "id_produto": "3"   // ID gerado para Leite
    }
    ```
    
4. **GET** http://localhost:5000/ordem para verificar.

---
