from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS

from models import Session, Produto
from schemas import (
    ProdutoSchema,
    ProdutoUpdateSchema,
    ProdutoBuscaSchema,
    ProdutoViewSchema,
    ListagemProdutosSchema,
    ProdutoDelSchema,
    ErrorSchema,
    apresenta_produto,
    apresenta_produtos
)
from logger import logger

info = Info(
    title="API de Estoque",
    version="1.0.0",
    description="API para cadastro, listagem, busca, atualização e remoção de produtos de estoque."
)

app = OpenAPI(__name__, info=info)
# Permite que o frontend se comunique com a API tanto via Live Server
# quanto abrindo o arquivo index.html diretamente no navegador.
CORS(app, supports_credentials=False)

@app.after_request
def apply_cors_headers(response):
    # Ajusta manualmente os cabeçalhos CORS para suportar origens locais,
    # incluindo o caso em que o frontend é aberto diretamente via file://.
    origin = request.headers.get("Origin")

    if origin == "null":
        response.headers["Access-Control-Allow-Origin"] = "null"
    elif origin:
        response.headers["Access-Control-Allow-Origin"] = origin
    else:
        response.headers["Access-Control-Allow-Origin"] = "*"

    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

home_tag = Tag(
    name="Documentação",
    description="Rotas relacionadas à documentação da API"
)

produto_tag = Tag(
    name="Produto",
    description="Cadastro, listagem, busca, atualização e remoção de produtos do estoque"
)


@app.get("/", tags=[home_tag])
def home():
    """Redireciona o usuário para a documentação Swagger da API."""
    return redirect("/openapi")


@app.post(
    "/produtos",
    tags=[produto_tag],
    summary="Cadastrar novo produto",
    responses={"201": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema}
)
def add_produto(body: ProdutoSchema):
    """Cadastra um novo produto no banco de dados.

    Recebe os dados enviados no corpo da requisição e cria um novo
    registro no estoque.
    """
    produto = Produto(
        nome=body.nome,
        categoria=body.categoria,
        quantidade=body.quantidade,
        unidade=body.unidade,
        preco=body.preco,
        descricao=body.descricao
    )

    logger.debug(f"Adicionando produto de nome: '{produto.nome}'")
    session = Session()

    try:
        session.add(produto)
        session.commit()
        session.refresh(produto)

        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 201

    except IntegrityError:
        # Faz rollback para evitar inconsistências caso haja conflito no banco.
        session.rollback()
        error_msg = "Produto de mesmo nome já salvo na base."
        logger.warning(f"Erro ao adicionar produto '{produto.nome}': {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível salvar o novo produto."
        logger.warning(f"Erro ao adicionar produto '{produto.nome}': {error_msg} | detalhe: {str(e)}")
        return {"message": error_msg}, 400

    finally:
        session.close()


@app.get(
    "/produtos",
    tags=[produto_tag],
    summary="Listar todos os produtos",
    responses={"200": ListagemProdutosSchema}
)
def get_produtos():
    """Retorna todos os produtos cadastrados no estoque."""
    logger.debug("Coletando produtos")
    session = Session()

    try:
        produtos = session.query(Produto).all()

        if not produtos:
            return {"produtos": []}, 200

        logger.debug(f"{len(produtos)} produtos encontrados")
        return apresenta_produtos(produtos), 200

    finally:
        session.close()


@app.get(
    "/produtos/<id>",
    tags=[produto_tag],
    summary="Buscar produto por ID",
    responses={"200": ProdutoViewSchema, "404": ErrorSchema}
)
def get_produto(path: ProdutoBuscaSchema):
    """Busca um produto específico a partir do ID informado na rota."""
    produto_id = path.id
    logger.debug(f"Coletando dados sobre produto #{produto_id}")
    session = Session()

    try:
        produto = session.query(Produto).filter(Produto.id == produto_id).first()

        if not produto:
            error_msg = "Produto não encontrado na base."
            logger.warning(f"Erro ao buscar produto '{produto_id}': {error_msg}")
            return {"message": error_msg}, 404

        logger.debug(f"Produto encontrado: '{produto.nome}'")
        return apresenta_produto(produto), 200

    finally:
        session.close()


@app.put(
    "/produtos/<id>",
    tags=[produto_tag],
    summary="Atualizar produto por ID",
    responses={"200": ProdutoViewSchema, "404": ErrorSchema, "400": ErrorSchema}
)
def update_produto(path: ProdutoBuscaSchema, body: ProdutoUpdateSchema):
    """Atualiza os dados de um produto já cadastrado."""
    produto_id = path.id
    logger.debug(f"Atualizando produto #{produto_id}")
    session = Session()

    try:
        produto = session.query(Produto).filter(Produto.id == produto_id).first()

        if not produto:
            error_msg = "Produto não encontrado na base."
            logger.warning(f"Erro ao atualizar produto '{produto_id}': {error_msg}")
            return {"message": error_msg}, 404

        produto.nome = body.nome
        produto.categoria = body.categoria
        produto.quantidade = body.quantidade
        produto.unidade = body.unidade
        produto.preco = body.preco
        produto.descricao = body.descricao

        session.commit()
        session.refresh(produto)

        logger.debug(f"Produto #{produto_id} atualizado com sucesso")
        return apresenta_produto(produto), 200

    except IntegrityError:
        session.rollback()
        error_msg = "Já existe outro produto com esse nome."
        logger.warning(f"Erro ao atualizar produto '{produto_id}': {error_msg}")
        return {"message": error_msg}, 400

    except Exception as e:
        session.rollback()
        error_msg = "Não foi possível atualizar o produto."
        logger.warning(f"Erro ao atualizar produto '{produto_id}': {error_msg} | detalhe: {str(e)}")
        return {"message": error_msg}, 400

    finally:
        session.close()


@app.delete(
    "/produtos/<id>",
    tags=[produto_tag],
    summary="Excluir produto por ID",
    responses={"200": ProdutoDelSchema, "404": ErrorSchema}
)
def del_produto(path: ProdutoBuscaSchema):
    """Remove um produto do estoque com base no ID informado."""
    produto_id = path.id
    logger.debug(f"Deletando produto #{produto_id}")
    session = Session()

    try:
        produto = session.query(Produto).filter(Produto.id == produto_id).first()

        if not produto:
            error_msg = "Produto não encontrado na base."
            logger.warning(f"Erro ao deletar produto '{produto_id}': {error_msg}")
            return {"message": error_msg}, 404

        session.delete(produto)
        session.commit()

        logger.debug(f"Deletado produto #{produto_id}")
        return {"message": "Produto removido com sucesso.", "id": produto_id}, 200

    finally:
        session.close()


if __name__ == "__main__":
    app.run(debug=True)