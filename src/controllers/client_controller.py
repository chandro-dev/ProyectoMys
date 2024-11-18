from fastapi import APIRouter, HTTPException,Body, Path, Query
from src.config import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from src.mappers.clients_mapper import PersonSchema
from src.services.clients_service import get_all_clients,get_client_by_id,update_client,delete_client,saveClient


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

@router.post("/clients",tags=['Clientes'])
def insert_client(person:PersonSchema = Body()):
    return saveClient(person)

# Agregar la ruta usando el método del controlador
@router.get("/clients",tags=['Clientes'])
def get_clients():
    return get_all_clients()

@router.get("/client/{idCLient}",tags=['Clientes'])
def get_client(idCLient:str = Path):
    return get_client_by_id(idCLient)

@router.put("/updateClient/{idClient}",tags=['Clientes'])
def updateClient(idClient:str = Path, bussiness:str = Path):
    return update_client(idClient,bussiness)

@router.delete("/deleteClient/{idClient}",tags=['Clientes'])
def deleteClient(idClient:str = Path):
    return delete_client(idClient)   