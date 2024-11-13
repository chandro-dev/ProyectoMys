from sqlalchemy import Column, Integer, String, DateTime
from src.config import Base
class Reminders(Base):
    __tablename__ = "recordatorios"  # Nombre de la tabla en la base de datos

    id = Column("id_recordatorio",String, primary_key=True, index=True)
    tittle = Column("titulo_recordatorio",String, index=True)
    description = Column("descripcion",String,index=True)
    seller_id = Column("id_vendedor",String, nullable=False)

    def __repr__(self):
        return f"<Task(name={self.tittle}, email={self.description})>"