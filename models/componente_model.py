from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False, unique=True)
    componentes = relationship('Componente', back_populates='categoria', cascade='all, delete-orphan')


class Componente(Base):
    __tablename__ = 'componentes'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(500), nullable=True)   # opcional: detalles del componente
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship('Categoria', back_populates='componentes')