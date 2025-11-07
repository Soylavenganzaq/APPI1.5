from repositories.componente_repository import ComponenteRepository
from models.componente_model import Componente
from sqlalchemy.orm import Session


class ComponenteService:
  
    def __init__(self, db_session: Session):
     
        self.repository = ComponenteRepository(db_session)

    def listar_componentes(self):
      
        return self.repository.get_all_componentes()

    # Compatibilidad con los nombres usados por el controlador
    def listar_computadores(self):
        return self.listar_componentes()

    def crear_computador(self, cpu: str, ram: int, almacenamiento: str, gpu: str = None, so: str = None):
        return self.repository.create_componente(cpu, ram, almacenamiento, gpu, so)

    def actualizar_computador(self, componente_id: int, cpu: str = None, ram: int = None, almacenamiento: str = None, gpu: str = None, so: str = None):
        return self.repository.update_componente(componente_id, cpu, ram, almacenamiento, gpu, so)

    def eliminar_computador(self, componente_id: int):
        return self.repository.delete_componente(componente_id)

    def obtener_componente(self, componente_id: int):
       
        return self.repository.get_componente_by_id(componente_id)

    def crear_componente(self, name: str):
        
        return self.repository.create_componente(name)

    def actualizar_componente(self, componente_id: int, name: str = None):
       
        return self.repository.update_componente(componente_id, name)

    def eliminar_componente(self, componente_id: int):
        
        return self.repository.delete_componente(componente_id)
