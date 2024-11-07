from fastapi import FastAPI
from src.controllers import client_controller

app = FastAPI()

# Incluir el enrutador de clientes
app.include_router(client_controller.router)

# Inicia la aplicación con: uvicorn app.main:app --reload
