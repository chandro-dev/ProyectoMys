from src.config import SessionLocal
from src.models.interactions_model import Interactions
from sqlalchemy.exc import SQLAlchemyError

# Crear una nueva interacción
def create_interaction(interaction_data: Interactions):
    session = SessionLocal()
    try:
        session.add(interaction_data)
        session.commit()
        session.refresh(interaction_data)
        return interaction_data
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error al crear la interacción: {str(e)}")
    finally:
        session.close()

# Eliminar una interacción
def delete_interaction(interaction_id: str):
    session = SessionLocal()
    try:
        interaction = session.query(Interactions).filter(Interactions.id == interaction_id).first()
        if not interaction:
            raise Exception("Interacción no encontrada")
        
        session.delete(interaction)
        session.commit()
        return {"message": "Interacción eliminada con éxito"}
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error al eliminar la interacción: {str(e)}")
    finally:
        session.close()

# Buscar interacciones por ID de cliente
def get_interactions_by_client_id(client_id: str):
    session = SessionLocal()
    try:
        interactions = session.query(Interactions).filter(Interactions.client_id == client_id).all()
        return interactions
    except SQLAlchemyError as e:
        raise Exception(f"Error al obtener interacciones por ID de cliente: {str(e)}")
    finally:
        session.close()

# Editar una interacción
def update_interaction(interaction_id: int, updated_data: Interactions):
    session = SessionLocal()
    try:
        interaction = session.query(Interactions).filter(Interactions.id == interaction_id).first()
        if not interaction:
            raise Exception("Interacción no encontrada")
        
        for key, value in updated_data.items():
            if hasattr(interaction, key):
                setattr(interaction, key, value)

        session.commit()
        session.refresh(interaction)
        return interaction
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error al actualizar la interacción: {str(e)}")
    finally:
        session.close()
