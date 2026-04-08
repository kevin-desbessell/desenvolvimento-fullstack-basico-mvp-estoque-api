"""Arquivo base para criação dos models do projeto."""

from sqlalchemy.orm import declarative_base

# Classe base usada pelo SQLAlchemy para mapear as tabelas do banco.
Base = declarative_base()