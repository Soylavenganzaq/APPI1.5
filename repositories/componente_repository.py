from models.componente_model import Componente
from sqlalchemy.orm import Session

class ComponenteRepository:
    
    

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_componentes(self):
      
        return self.db.query(Componente).all()

    def get_componente_by_id(self, componente_id: int):
      
        return self.db.query(Componente).filter(Componente.id == componente_id).first()

    def create_componente(self, name: str):
       
        new_componente = Componente(name=name)
        self.db.add(new_componente)
        self.db.commit()
        self.db.refresh(new_componente)
        return new_componente

    def update_componente(self, componente_id: int, name: str = None):
       
        componente = self.get_componente_by_id(componente_id)
        if componente and name:
            componente.name = name
            self.db.commit()
            self.db.refresh(componente)
        return componente

    def delete_componente(self, componente_id: int):
      
        componente = self.get_componente_by_id(componente_id)
        if componente:
            self.db.delete(componente)
            self.db.commit()
        return componente