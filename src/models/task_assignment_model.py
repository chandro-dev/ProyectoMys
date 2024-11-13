from sqlalchemy import Column, Integer, String, DateTime
from src.config import Base
class Task(Base):
    __tablename__ = "asignacion_de_tareas"  # Nombre de la tabla en la base de datos

    id = Column("id_tarea",Integer, primary_key=True, index=True)
    tittle = Column("titulo",String, index=True)
    description = Column("descripcion",String,index=True)
    person_id = Column("id_persona",String, nullable=False)
    creation_date = Column("fecha_creacion",DateTime, nullable=True)
    end_date = Column("fecha_finalizacion",DateTime, nullable=True)
    administration_id = Column("id_administrador",Integer, nullable=True)

    def __repr__(self):
        return f"<Task(name={self.tittle}, email={self.description})>"