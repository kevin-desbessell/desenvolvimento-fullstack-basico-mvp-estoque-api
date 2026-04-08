from pydantic import BaseModel, Field
from typing import Optional, List

from models.produto import Produto


class ProdutoSchema(BaseModel):
    """Schema utilizado no cadastro de um novo produto do estoque."""
    nome: str = Field(
        "Cimento CP II",
        description="Nome do produto cadastrado no estoque."
    )
    categoria: str = Field(
        "Cimento",
        description="Categoria à qual o produto pertence."
    )
    quantidade: int = Field(
        100,
        description="Quantidade disponível no estoque.",
        ge=0
    )
    unidade: str = Field(
        "saco",
        description="Unidade de medida do produto, como saco, unidade, caixa ou metro."
    )
    preco: float = Field(
        42.90,
        description="Preço unitário do produto.",
        ge=0
    )
    descricao: Optional[str] = Field(
        "Saco de 50kg",
        description="Descrição complementar do produto."
    )


class ProdutoUpdateSchema(BaseModel):
    """Schema utilizado na atualização de um produto já cadastrado."""
    nome: str = Field(
        "Cimento CP II Atualizado",
        description="Novo nome do produto."
    )
    categoria: str = Field(
        "Cimento",
        description="Nova categoria do produto."
    )
    quantidade: int = Field(
        80,
        description="Nova quantidade disponível no estoque.",
        ge=0
    )
    unidade: str = Field(
        "saco",
        description="Nova unidade de medida do produto."
    )
    preco: float = Field(
        44.50,
        description="Novo preço unitário do produto.",
        ge=0
    )
    descricao: Optional[str] = Field(
        "Produto atualizado",
        description="Nova descrição complementar do produto."
    )


class ProdutoBuscaSchema(BaseModel):
    """Schema utilizado para buscar um produto pelo seu identificador."""
    id: int = Field(
        1,
        description="Identificador único do produto."
    )


class ProdutoViewSchema(BaseModel):
    """Schema de resposta com os dados completos de um produto."""
    id: int = Field(
        1,
        description="Identificador único do produto."
    )
    nome: str = Field(
        "Cimento CP II",
        description="Nome do produto."
    )
    categoria: str = Field(
        "Cimento",
        description="Categoria do produto."
    )
    quantidade: int = Field(
        100,
        description="Quantidade disponível no estoque."
    )
    unidade: str = Field(
        "saco",
        description="Unidade de medida do produto."
    )
    preco: float = Field(
        42.90,
        description="Preço unitário do produto."
    )
    descricao: Optional[str] = Field(
        "Saco de 50kg",
        description="Descrição complementar do produto."
    )
    data_insercao: Optional[str] = Field(
        "2026-04-08 17:00:00",
        description="Data e hora em que o produto foi inserido no sistema."
    )


class ListagemProdutosSchema(BaseModel):
    """Schema de resposta para a listagem de produtos."""
    produtos: List[ProdutoViewSchema] = Field(
        ...,
        description="Lista de produtos cadastrados no estoque."
    )


class ProdutoDelSchema(BaseModel):
    """Schema de resposta após a remoção de um produto."""
    message: str = Field(
        "Produto removido com sucesso.",
        description="Mensagem de confirmação da remoção."
    )
    id: int = Field(
        1,
        description="Identificador do produto removido."
    )


def apresenta_produtos(produtos: List[Produto]):
    """Converte uma lista de produtos do banco para o formato de resposta da API."""
    result = []

    for produto in produtos:
        result.append({
            "id": produto.id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "quantidade": produto.quantidade,
            "unidade": produto.unidade,
            "preco": produto.preco,
            "descricao": produto.descricao,
            "data_insercao": produto.data_insercao.strftime("%Y-%m-%d %H:%M:%S") if produto.data_insercao else None
        })

    return {"produtos": result}


def apresenta_produto(produto: Produto):
    """Converte um produto do banco para o formato de resposta da API."""
    return {
        "id": produto.id,
        "nome": produto.nome,
        "categoria": produto.categoria,
        "quantidade": produto.quantidade,
        "unidade": produto.unidade,
        "preco": produto.preco,
        "descricao": produto.descricao,
        "data_insercao": produto.data_insercao.strftime("%Y-%m-%d %H:%M:%S") if produto.data_insercao else None
    }