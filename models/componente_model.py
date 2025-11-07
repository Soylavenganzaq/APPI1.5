from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Componente(Base):
    __tablename__ = 'componentes'
    id = Column(Integer, primary_key=True, index=True)
    cpu = Column(String(255), nullable=False)
    ram = Column(Integer, nullable=False)
    almacenamiento = Column(String(255), nullable=False)
    gpu = Column(String(255), nullable=True)
    so = Column(String(255), nullable=True)