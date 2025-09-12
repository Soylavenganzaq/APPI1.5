from models.componente_model import Componente
from sqlalchemy.orm import Session

class ComponenteRepository:
    """
    Repositorio para la gestión de componentes de PC en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar componentes.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_componentes(self):
        """
        Recupera todos los componentes de PC almacenados en la base de datos.
        Utiliza una consulta ORM para obtener todas las instancias de la clase Componente,
        permitiendo así listar todos los componentes registrados en el sistema.
        """
        return self.db.query(Componente).all()

    def get_componente_by_id(self, componente_id: int):
        """
        Busca y retorna un componente específico según su identificador único (ID).
        Realiza una consulta filtrando por el campo 'id' de la tabla Componente.
        Devuelve la instancia de Componente si existe, o None si no se encuentra.
        """
        return self.db.query(Componente).filter(Componente.id == componente_id).first()

    def create_componente(self, name: str):
        """
        Crea y almacena un nuevo componente de PC en la base de datos.
        Recibe el nombre del componente como parámetro, instancia un nuevo objeto Componente
        y lo agrega a la sesión de la base de datos. Tras confirmar la transacción,
        retorna el nuevo componente creado, incluyendo su ID asignado automáticamente.
        """
        new_componente = Componente(name=name)
        self.db.add(new_componente)
        self.db.commit()
        self.db.refresh(new_componente)
        return new_componente

    def update_componente(self, componente_id: int, name: str = None):
        """
        Actualiza la información de un componente existente en la base de datos.
        Permite modificar el nombre del componente identificado por su ID. 
        Si el componente existe y se proporciona un nuevo nombre, se actualiza el registro.
        Devuelve la instancia del componente actualizada o None si no se encuentra.
        """
        componente = self.get_componente_by_id(componente_id)
        if componente and name:
            componente.name = name
            self.db.commit()
            self.db.refresh(componente)
        return componente

    def delete_componente(self, componente_id: int):
        """
        Elimina un componente de PC de la base de datos según su identificador único (ID).
        Busca el componente correspondiente y, si existe, lo elimina de la base de datos.
        Devuelve la instancia del componente eliminado o None si no se encuentra.
        """
        componente = self.get_componente_by_id(componente_id)
        if componente:
            self.db.delete(componente)
            self.db.commit()
        return componente