from pydantic import BaseModel, Field
from src.services.generations_service import id_generation
from src.models.interactions_model import Interactions

class Interactions(BaseModel):
    interactionsType: int 
    clienteId: str = Field(max_length=10)

    class Config:
        orm_mode = True
    def to_database_model(self) -> Interactions:
        idInteraction=id_generation()
        return Interactions(
            id=idInteraction,
            interactions_type=self.interactionsType,
            cliente_id=self.clienteId
        )