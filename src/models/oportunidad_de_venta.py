from sqlalchemy import Column, Integer, String, DateTime
from src.config import Base
class Ventas(Base):
    __tablename__ = "oportunidades_de_ventas"  # Nombre de la tabla en la base de datos

    idOportuninity = Column("id_oportunidad",Integer, primary_key=True, index=True)
    description = Column("descripcion",String, index=True)
    value = Column("valor_estimado",Integer,index=True)
    deadline = Column("fecha_de_cierre",Datetime, nullable=False)
    etapa = Column("etapa_de_venta",Integer, nullable=True)
    note = Column("notas",String, nullable=True)
    sourceOpportunity = Column("fuente_de_la_oportunidad",String, nullable=True)
    clientId = Column("id_cliente",String, nullable=True)
    sellerId = Column("id_vendedor",String, nullable=True)

    def __repr__(self):
        return f"<Ventas(description={self.description}, value={self.value})>"
