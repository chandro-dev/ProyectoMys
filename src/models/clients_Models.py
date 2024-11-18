from sqlalchemy import Column, Integer, String
from src.config import Base
class Clients(Base):
    __tablename__ = "clientes"  # Nombre de la tabla en la base de datos

    client_id = Column("id_cliente",String, primary_key=True, index=True)
    user_id = Column("id_usuario",String, index=True)
    bussiness = Column("empresa",String,index=True)

    def __repr__(self):
        return f"<Clients(name={self.client_id}, email={self.bussiness})>"