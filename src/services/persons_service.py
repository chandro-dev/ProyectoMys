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

def update_person(person_id:str,person_data:Person):
    session = SessionLocal()
    try:
        # Buscar la persona por su ID
        person = session.query(Person).filter(Person.id == person_id).first()
        if not person:
            raise Exception("Persona no encontrada")

        # Actualizar los campos con los datos proporcionados
        for key, value in person_data.items():
            if hasattr(person, key):
                setattr(person, key, value)

        # Confirmar los cambios en la base de datos
        session.commit()
        session.refresh(person)

        return person
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error al actualizar la persona: {e}")
    finally:
        session.close()

def get_all():
    try:    
        session = SessionLocal()
        return session.query(Person).all()
    except SQLAlchemyError as e:
        raise Exception(f"Error al obtener los datos personales: {e}")