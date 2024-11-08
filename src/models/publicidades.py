from sqlalchemy import Column, Integer, String, DateTime
from src.config import Base
class Publicidad(Base):
    __tablename__ = "publicidades"  # Nombre de la tabla en la base de datos

    id = Column("id_publicidad",Integer, primary_key=True, index=True)
    title = Column("titulo",String, index=True)
    description = Column("descripcion",String,index=True)
    file = Column("archivo_adjunto",String, nullable=False)
    clientId = Column("id_cliente",String, nullable=True)
    merketingId = Column("id_marketing",String, nullable=True)

    def __repr__(self):
        return f"<Publicidad(name={self.title}, email={self.description})>"
