from fastapi import FastAPI
from src.controllers import client_controller
from src.controllers import sells_controller
from src.controllers import person_controller
from src.controllers import interactions_controller
from src.controllers import task_controller

app = FastAPI()

# Incluir el enrutador de clientes
app.include_router(client_controller.router)
app.include_router(sells_controller.router)
app.include_router(person_controller.router)
app.include_router(interactions_controller.router)
app.include_router(task_controller.router)
# Inicia la aplicación con: uvicorn app.main:app --reload
