from fastapi import APIRouter, HTTPException,Body, Path
from src.mappers.interactions_mapper import Interactions
from src.services.interactions_service import create_interaction,delete_interaction,get_interactions_by_client_id,update_interaction

router = APIRouter()

@router.post("/interactions", tags=['Interacciones'])
def save_interaction(interactions:Interactions = Body()):
    return create_interaction(interactions.to_database_model())

@router.get("/interactions/{client}",tags=['Interacciones'])
def getInteractions(client:str=Path):
    return get_interactions_by_client_id(client)

@router.delete("/deleteInteractions/{id}",tags=['Interacciones'])
def deleteSalesOportunity(id:str=Path):
    return delete_interaction(id)

@router.put("/updateInteractions/{idInteraction}",tags=['Interacciones'])
def updateStatus(idInteraction:int=Path,interaction:Interactions=Body()):
    return update_interaction(idInteraction,interaction.to_database_model)