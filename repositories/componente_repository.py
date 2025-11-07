from models.componente_model import Componente
from sqlalchemy.orm import Session

class ComponenteRepository:
    
    

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_componentes(self):
        return self.db.query(Componente).all()

    def get_componente_by_id(self, componente_id: int):
        return self.db.query(Componente).filter(Componente.id == componente_id).first()

    def create_componente(self, cpu: str, ram: int, almacenamiento: str, gpu: str = None, so: str = None):
        new_componente = Componente(cpu=cpu, ram=ram, almacenamiento=almacenamiento, gpu=gpu, so=so)
        self.db.add(new_componente)
        self.db.commit()
        self.db.refresh(new_componente)
        return new_componente

    def update_componente(self, componente_id: int, cpu: str = None, ram: int = None, almacenamiento: str = None, gpu: str = None, so: str = None):
        componente = self.get_componente_by_id(componente_id)
        if componente:
            if cpu is not None: componente.cpu = cpu
            if ram is not None: componente.ram = ram
            if almacenamiento is not None: componente.almacenamiento = almacenamiento
            if gpu is not None: componente.gpu = gpu
            if so is not None: componente.so = so
            self.db.commit()
            self.db.refresh(componente)
        return componente

    def delete_componente(self, componente_id: int):
        componente = self.get_componente_by_id(componente_id)
        if componente:
            self.db.delete(componente)
            self.db.commit()
        return componente