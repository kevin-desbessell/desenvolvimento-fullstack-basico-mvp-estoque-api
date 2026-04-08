from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from models.base import Base


class Produto(Base):
    """Model que representa um produto cadastrado no estoque."""

    __tablename__ = "produtos"

    id = Column("pk_produto", Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), unique=True, nullable=False)
    categoria = Column(String(80), nullable=False)
    quantidade = Column(Integer, nullable=False)
    unidade = Column(String(20), nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String(255), nullable=True)
    data_insercao = Column(DateTime, default=datetime.now)

    def __init__(
        self,
        nome: str,
        categoria: str,
        quantidade: int,
        unidade: str,
        preco: float,
        descricao: str | None = None,
        data_insercao: Union[DateTime, None] = None
    ):
        """Cria uma nova instância de produto.

        Args:
            nome: Nome do produto.
            categoria: Categoria à qual o produto pertence.
            quantidade: Quantidade disponível em estoque.
            unidade: Unidade de medida do produto.
            preco: Preço unitário do produto.
            descricao: Descrição complementar do produto.
            data_insercao: Data de inserção do produto no sistema.
        """
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.unidade = unidade
        self.preco = preco
        self.descricao = descricao

        if data_insercao:
            self.data_insercao = data_insercao