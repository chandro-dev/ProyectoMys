from fastapi import APIRouter, HTTPException
from src.config import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

router = APIRouter()


class ClientController:
    def __init__(self):
        # Crear una sesión de base de datos al inicializar la clase
        self.db: Session = SessionLocal()
        
        # Intentar ejecutar una consulta para verificar la conexión
        try:
            self.db.execute(text("SELECT 1"))
        except SQLAlchemyError as e:
            self.db.close()  # Cierra la sesión si hay un error
            raise HTTPException(status_code=500, detail="Error de conexión a la base de datos") from e
    def get_tables(self):
        result = self.db.execute(text("SELECT * FROM public.tipos_de_interacciones")).fetchall()
        formatted_result = [row[1] for row in result]  # Extraemos solo el nombre de la tabla
        return {"tables": formatted_result}

# Crear una instancia del controlador y añadir sus rutas al router
client_controller = ClientController()


# Agregar la ruta usando el método del controlador
@router.get("/status")
def get_status():
    return client_controller.get_tables()