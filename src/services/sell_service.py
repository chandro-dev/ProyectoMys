from src.config import SessionLocal
from src.models.sales_opportunity import Sales_opportunity
from sqlalchemy.exc import SQLAlchemyError

def save_sales_opportunity(sales_opportunity_data: Sales_opportunity):
    # Creamos una nueva sesión
    session = SessionLocal()
    
    try:
        # Añadimos el objeto Sales_opportunity a la sesión
        session.add(sales_opportunity_data)
        # Confirmamos (commit) los cambios para guardar el objeto en la base de datos
        session.commit()
        # Refrescamos para obtener el ID generado, si es necesario
        session.refresh(sales_opportunity_data)
        return sales_opportunity_data
    except Exception as e:
        # Si ocurre un error, revertimos los cambios
        session.rollback()
        print(f"Error al guardar la oportunidad de venta: {e}")
        return None
    finally:
        # Cerramos la sesión
        session.close()

def get_sales_opportunities_by_stage(stage_id: int):
    session = SessionLocal()
    try:
        # Filtra las oportunidades de venta por el campo `etapa`
        opportunities = session.query(Sales_opportunity).filter(Sales_opportunity.etapa == stage_id).all()
        return opportunities
    except SQLAlchemyError as e:
        print(f"Error al buscar oportunidades de ventas por etapa: {e}")
        return []
    finally:
        session.close()

def get_all_sales_opportunities():
    session = SessionLocal()
    try:
        # Consulta todas las oportunidades de ventas en la tabla
        opportunities = session.query(Sales_opportunity).all()
        return opportunities
    except SQLAlchemyError as e:
        print(f"Error al obtener todas las oportunidades de ventas: {e}")
        return []
    finally:
        session.close()

def delete_sales_opportunity(opportunity_id: str):
    session = SessionLocal()
    try:
        # Busca la oportunidad de ventas por ID
        opportunity = session.query(Sales_opportunity).filter(Sales_opportunity.idOportuninity == opportunity_id).first()
        if opportunity:
            # Elimina la oportunidad de ventas
            session.delete(opportunity)
            session.commit()
            return True
        else:
            print("Oportunidad de ventas no encontrada.")
            return False
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al eliminar la oportunidad de ventas: {e}")
        return False
    finally:
        session.close()

def update_sales_opportunity_status(opportunity_id: str, new_status: str):
    session = SessionLocal()
    try:
        # Busca la oportunidad de ventas por ID
        opportunity = session.query(Sales_opportunity).filter(Sales_opportunity.idOportuninity == opportunity_id).first()
        if opportunity:
            # Actualiza solo el campo `status`
            opportunity.status = new_status
            session.commit()
            session.refresh(opportunity)
            return opportunity
        else:
            print("Oportunidad de ventas no encontrada.")
            return None
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al actualizar el estado de la oportunidad de ventas: {e}")
        return None
    finally:
        session.close()