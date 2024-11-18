from src.config import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from src.models.persons_models import Person
from src.models.clients_Models import Clients
from src.services.persons_service import save_person
from src.mappers.clients_mapper import PersonSchema

def saveClient(person: PersonSchema):
    db = SessionLocal()
    try:
        # Convertir el esquema a modelo de base de datos
        personGenerate = person.to_database_model()
        if not personGenerate:
            raise ValueError("No se pudo generar el modelo de persona desde el esquema")

        # Guardar la entidad 'Persona' en la base de datos
        save_person(personGenerate) 

        # Crear el cliente asociado
        client = person.to_client_model(personGenerate)
        db.add(client)
        db.commit()
        db.refresh(client)

        return client
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error al guardar el cliente: {e}")
    finally:
        db.close()

    


# Obtener todos los clientes
def get_all_clients():
    try:
        db=SessionLocal()
        return db.query(Clients).all()
    except SQLAlchemyError as e:
        raise Exception(f"Error al obtener los clientes: {e}")

# Obtener un cliente por ID
def get_client_by_id(client_id):
    try:
        db=SessionLocal()
        return db.query(Clients).filter(Clients.id == client_id).first()
    except SQLAlchemyError as e:
        raise Exception(f"Error al obtener el cliente: {e}")

# Actualizar empresa de un cliente
def update_client(client_id, bussiness):
    try:
        db=SessionLocal()
        client = db.query(Clients).filter(Clients.id == client_id).first()
        if not client:
            raise Exception("Cliente no encontrado")
        client.bussiness=bussiness
        db.commit()
        db.refresh(client)
        return client
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error al actualizar el cliente: {e}")

# Eliminar un cliente
def delete_client(client_id):
    try:
        db=SessionLocal()
        client = db.query(Clients).filter(Clients.id == client_id).first()
        if not client:
            raise Exception("Cliente no encontrado")
        db.delete(client)
        db.commit()
        return {"message": "Cliente eliminado correctamente"}
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error al eliminar el cliente: {e}")