"""Configuração de conexão com o banco e criação da sessão do SQLAlchemy."""

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

from models.base import Base
from models.produto import Produto

db_path = "database"

# Garante que a pasta do banco exista antes de iniciar a aplicação.
if not os.path.exists(db_path):
    os.makedirs(db_path)

# URL de conexão com o banco SQLite local.
db_url = f"sqlite:///{db_path}/db.sqlite3"

# Engine principal usada nas operações com o banco.
engine = create_engine(
    db_url,
    echo=False,
    connect_args={"check_same_thread": False}
)

# Sessão utilizada pelas rotas da aplicação.
Session = sessionmaker(bind=engine)

# Cria o banco caso ele ainda não exista.
if not database_exists(engine.url):
    create_database(engine.url)

# Cria as tabelas definidas nos models.
Base.metadata.create_all(engine)