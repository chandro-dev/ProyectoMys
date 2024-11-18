from src.config import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from src.models.persons_models import Person

def save_person(person_data: Person):
    # Creamos una nueva sesión
    session = SessionLocal()
    
    try:
        # Añadimos el objeto Sales_opportunity a la sesión
        session.add(person_data)
        # Confirmamos (commit) los cambios para guardar el objeto en la base de datos
        session.commit()
        # Refrescamos para obtener el ID generado, si es necesario
        session.refresh(person_data)
        return person_data
    except Exception as e:
        # Si ocurre un error, revertimos los cambios
        session.rollback()
        print(f"Error al guardar la persona: {e}")
        return None
    finally:
        # Cerramos la sesión2   
        session.close()