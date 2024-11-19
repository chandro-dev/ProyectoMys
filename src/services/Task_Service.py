from src.config import SessionLocal
from src.models.task_assignment_model import Task
from sqlalchemy.exc import SQLAlchemyError

# Crear una nueva tarea
def create_task(task_data: Task):
    session = SessionLocal()
    try:
        session.add(task_data)
        session.commit()
        session.refresh(task_data)
        return task_data
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error al crear la tarea: {str(e)}")
    finally:
        session.close()

# Actualizar una tarea existente
def update_task(task_id: str, updated_data: Task):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise Exception("Tarea no encontrada")
        
        for key, value in updated_data.items():
            if hasattr(task, key):
                setattr(task, key, value)

        session.commit()
        session.refresh(task)
        return task
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error al actualizar la tarea: {str(e)}")
    finally:
        session.close()

# Eliminar una tarea
def delete_task(task_id: int):
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise Exception("Tarea no encontrada")
        
        session.delete(task)
        session.commit()
        return {"message": "Tarea eliminada con éxito"}
    except SQLAlchemyError as e:
        session.rollback()
        raise Exception(f"Error al eliminar la tarea: {str(e)}")
    finally:
        session.close()

# Obtener todas las tareas
def get_all_tasks():
    session = SessionLocal()
    try:
        tasks = session.query(Task).all()
        return tasks
    except SQLAlchemyError as e:
        raise Exception(f"Error al obtener las tareas: {str(e)}")
    finally:
        session.close()

# Filtrar tareas por `person_id` (ID del vendedor)
def get_tasks_by_person_id(person_id: str):
    session = SessionLocal()
    try:
        tasks = session.query(Task).filter(Task.person_id == person_id).all()
        return tasks
    except SQLAlchemyError as e:
        raise Exception(f"Error al obtener las tareas por ID de persona: {str(e)}")
    finally:
        session.close()
