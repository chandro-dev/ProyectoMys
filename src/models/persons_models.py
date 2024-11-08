from sqlalchemy import Column, Integer, String, DateTime
from src.config import Base
class Person(Base):
    __tablename__ = "personas"  # Nombre de la tabla en la base de datos

    id = Column("id_persona",Integer, primary_key=True, index=True)
    name = Column("primer_nombre",String, index=True)
    secondName = Column("segundo_nombre",String,index=True)
    lastname = Column("primer_apellido",String, nullable=False)
    secondLastName = Column("segundo_apellido",String, nullable=True)
    email = Column("correo",String, nullable=True)
    numberPhone = Column("telefono",String, nullable=True)

    def __repr__(self):
        return f"<Person(name={self.name}, email={self.email})>"