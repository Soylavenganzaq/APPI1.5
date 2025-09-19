from repositories.componente_repository import ComponenteRepository
from models.componente_model import Componente
from sqlalchemy.orm import Session


class ComponenteService:
  
    def __init__(self, db_session: Session):
     
        self.repository = ComponenteRepository(db_session)

    def listar_componentes(self):
      
        return self.repository.get_all_componentes()

    def obtener_componente(self, componente_id: int):
       
        return self.repository.get_componente_by_id(componente_id)

    def crear_componente(self, name: str):
        
        return self.repository.create_componente(name)

    def actualizar_componente(self, componente_id: int, name: str = None):
       
        return self.repository.update_componente(componente_id, name)

    def eliminar_componente(self, componente_id: int):
        
        return self.repository.delete_componente(componente_id)
