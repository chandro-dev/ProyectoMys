from sqlalchemy import Column, Integer, String, DateTime
from app.config import Base
class Interactions(Base):
    __tablename__ = "interacciones"  # Nombre de la tabla en la base de datos

    id = Column("id_interaccion",String, primary_key=True, index=True)
    interactions_type = Column("tipo_interaccion",Integer, index=True)
    cliente_id = Column("id_cliente",String,index=True)

    def __repr__(self):
        return f"<Interacciones(name={self.interactions_type}, email={self.cliente_id})>"