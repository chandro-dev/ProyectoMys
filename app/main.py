from fastapi import FastAPI
from app.controllers import client_controller
from app.controllers import sells_controller
from app.controllers import person_controller
from app.controllers import interactions_controller
from app.controllers import task_controller

app = FastAPI()

# Incluir el enrutador de clientes
app.include_router(client_controller.router)
app.include_router(sells_controller.router)
app.include_router(person_controller.router)
app.include_router(interactions_controller.router)
app.include_router(task_controller.router)
# Inicia la aplicación con: uvicorn app.main:app --reload
