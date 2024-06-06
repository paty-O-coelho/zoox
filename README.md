# 🚀 Cadastro API

Bem-vindo à API de Cadastro! Esta API permite gerenciar cadastros com operações de criação, leitura, atualização, exclusão e importação de dados.

## 🌟 Funcionalidades

- 📑 **Criar Cadastro**: Cria um novo cadastro na base de dados.
- 📋 **Listar Cadastros**: Lista todos os cadastros existentes.
- 🔍 **Buscar Cadastro**: Busca um cadastro específico pelo ID.
- ✏️ **Atualizar Cadastro**: Atualiza informações de um cadastro existente.
- 🗑️ **Excluir Cadastro**: Exclui um cadastro pelo ID.
- 📂 **Importar Cadastros**: Importa cadastros a partir de um arquivo CSV.

## 🛠️ Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)

## 📚 Endpoints da API

- 📋 **Listar Cadastros**
  - URL: /
  - Método HTTP: GET
  - Status de Sucesso: 200 OK

- 🔍 **Buscar Cadastro**
  - URL: /{cadastro_id}
  - Método HTTP: GET

- ✏️ **Atualizar Cadastro**
  - URL: /{cadastro_id}
  - Método HTTP: PUT

- 🗑️ **Excluir Cadastro**
  - URL: /{cadastro_id}
  - Método HTTP: DELETE

- 📂 **Importar Cadastros**
  - URL: /import
  - Método HTTP: POST
  - Status de Sucesso: 201 Created

## 🚀 Como Executar o Projeto

1. Clone o repositório:
   ```sh
   git clone https://github.com/paty-O-coelho/zoox.git
2. Navegue até o diretório do projeto:
   ```sh
   cd zoox
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
4. Crie as tabelas:
   ```sh
   python criar_tabelas.py
5. Execute a aplicação:
   ```sh
   python main.py
6. Acesse a documentação interativa da API em http://127.0.0.1:8000/docs.


## 💡 Swagger do projeto

![Descrição do GIF](zoox_api.gif)


## 🐘🎲 Banco com os dados cadastrados
![image](https://github.com/paty-O-coelho/zoox/assets/43469465/560e2357-9174-476b-8349-b0c8ee43fe31)


