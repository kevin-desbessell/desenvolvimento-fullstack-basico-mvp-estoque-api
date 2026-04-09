# API de Estoque

Backend de uma aplicação web simples para gerenciamento de estoque de uma loja de materiais de construção.

Este projeto foi desenvolvido como parte do MVP acadêmico da pós-graduação em Desenvolvimento Full Stack da PUC - Rio. A proposta da API é permitir operações básicas de cadastro, listagem, busca, atualização e remoção de produtos, utilizando **Python**, **Flask**, **SQLite** e documentação interativa com **Swagger**.

---

## Objetivo do projeto

A API foi criada para servir como backend de um sistema de controle de estoque simples, com foco em organização, clareza de código, documentação e separação de responsabilidades.

A aplicação permite:

- cadastrar produtos no estoque
- listar todos os produtos cadastrados
- buscar um produto específico por ID
- atualizar os dados de um produto
- remover produtos do estoque
- testar todas as rotas pela documentação Swagger

---

## Tecnologias utilizadas

- Python
- Flask
- Flask-Cors
- flask-openapi3
- SQLAlchemy
- SQLite

---

## Estrutura do projeto

```txt
estoque-api/
├── app.py
├── logger.py
├── requirements.txt
├── README.md
├── .gitignore
├── database/
│   └── db.sqlite3
├── log/
├── models/
│   ├── __init__.py
│   ├── base.py
│   └── produto.py
├── schemas/
│   ├── __init__.py
│   ├── error.py
│   └── produto.py
└── venv/
```

### Descrição das pastas e arquivos

- **app.py**: arquivo principal da aplicação, onde a API é iniciada e as rotas são definidas
- **logger.py**: configuração de logs da aplicação
- **models/**: definição do banco de dados e do model `Produto`
- **schemas/**: schemas utilizados na validação, documentação e serialização das respostas
- **database/**: local onde o banco SQLite é criado automaticamente
- **log/**: local onde os arquivos de log são gerados automaticamente

---

## Funcionalidades da API

### Produtos

- cadastrar novo produto
- listar todos os produtos
- buscar produto por ID
- atualizar produto por ID
- excluir produto por ID

### Documentação

- redirecionamento automático da rota inicial para o Swagger
- documentação interativa disponível via navegador

---

## Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- **Python 3.10 ou superior**
- **Git**

Para verificar se o Python está instalado:

```bash
python --version
```

ou

```bash
python3 --version
```

---

## Como clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd estoque-api
```

> Substitua `URL_DO_REPOSITORIO` pela URL real do seu repositório no GitHub.

---

## Como configurar o ambiente virtual

### Windows - PowerShell

Criar o ambiente virtual:

```powershell
python -m venv venv
```

Ativar o ambiente virtual:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### Windows - CMD

Criar o ambiente virtual:

```cmd
python -m venv venv
```

Ativar o ambiente virtual:

```cmd
venv\Scripts\activate.bat
```

---

### macOS e Linux - bash / zsh

Criar o ambiente virtual:

```bash
python3 -m venv venv
```

Ativar o ambiente virtual:

```bash
source venv/bin/activate
```

---

### macOS e Linux - fish shell

Criar o ambiente virtual:

```fish
python3 -m venv venv
```

Ativar o ambiente virtual:

```fish
source venv/bin/activate.fish
```

---

## Como instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

---

## Como executar o projeto

Depois de instalar as dependências, rode o comando:

```bash
python app.py
```

A aplicação será iniciada localmente.

---

## Como acessar a documentação Swagger

Com a API em execução, acesse no navegador:

```txt
http://127.0.0.1:5000/openapi
```

A rota inicial da aplicação:

```txt
http://127.0.0.1:5000/
```

redireciona automaticamente para a documentação.

---

## Banco de dados

O projeto utiliza **SQLite** como banco de dados local.

O arquivo do banco é criado automaticamente em:

```txt
database/db.sqlite3
```

Não é necessário criar o banco manualmente.

---

## Logs da aplicação

Os arquivos de log são gerados automaticamente na pasta:

```txt
log/
```

Esses arquivos ajudam no acompanhamento de execução, erros e eventos da API.

---

## Rotas principais

| Método | Rota             | Descrição |
|--------|------------------|-----------|
| GET    | `/`              | Redireciona para o Swagger |
| POST   | `/produtos`      | Cadastra um novo produto |
| GET    | `/produtos`      | Lista todos os produtos |
| GET    | `/produtos/{id}` | Busca um produto por ID |
| PUT    | `/produtos/{id}` | Atualiza um produto por ID |
| DELETE | `/produtos/{id}` | Remove um produto por ID |

---

## Exemplo de JSON para cadastro de produto

```json
{
  "nome": "Cimento CP II",
  "categoria": "Cimento",
  "quantidade": 100,
  "unidade": "saco",
  "preco": 42.9,
  "descricao": "Saco de 50kg"
}
```

---

## Exemplo de resposta de sucesso

```json
{
  "id": 1,
  "nome": "Cimento CP II",
  "categoria": "Cimento",
  "quantidade": 100,
  "unidade": "saco",
  "preco": 42.9,
  "descricao": "Saco de 50kg",
  "data_insercao": "2026-04-08 18:00:00"
}
```

---

## Exemplo de resposta de erro

```json
{
  "message": "Produto não encontrado na base."
}
```

---

## Códigos de status esperados

### Sucesso

- **200 OK**: requisição realizada com sucesso
- **201 Created**: recurso criado com sucesso

### Erros

- **400 Bad Request**: erro na requisição
- **404 Not Found**: recurso não encontrado
- **409 Conflict**: conflito de dados, como produto duplicado

---

## Organização e boas práticas utilizadas

Este backend foi estruturado com foco em:

- separação de responsabilidades
- organização em pastas
- documentação automática com Swagger
- validação de dados com schemas
- persistência local com SQLite
- manutenção simples e clara para fins acadêmicos

---

## Observações importantes

- este repositório contém apenas o **backend** do projeto
- o **frontend** deve ficar em um repositório separado
- o banco e os logs são gerados automaticamente ao executar a aplicação
- a documentação Swagger já permite testar todas as rotas sem necessidade de ferramentas externas
- a API foi configurada com CORS para permitir a comunicação com o frontend local
- o frontend pode ser aberto diretamente pelo arquivo `index.html` ou por um servidor local como Live Server

---

## Como desativar o ambiente virtual

Quando terminar o uso do projeto, execute:

```bash
deactivate
```

---

## Autor

Projeto desenvolvido por **Kevin Desbessell** como atividade acadêmica do curso de pós-graduação em **Desenvolvimento Full Stack** na Universidade PUC - Rio.