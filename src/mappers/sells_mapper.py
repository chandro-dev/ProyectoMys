from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from src.models.sales_opportunity import Sales_opportunity
from src.services.generations_service import id_generation,nullState

class SalesOpportunitySchema(BaseModel):
    description: str = Field(max_length=255)
    value: int = Field(..., description="El campo valor es obligatorio")
    deadline: datetime
    etapa: Optional[int] = None
    note: Optional[str] = None
    sourceOpportunity: Optional[str] = None
    clientId: str = Field(..., description="El campo cliente es obligatorio",max_length=10)
    sellerId: str = Field(..., description="El campo vendedor es obligatorio", max_length=10)

    class Config:
        orm_mode = True
    def to_database_model(self) -> Sales_opportunity:
        idSell=id_generation()
        return Sales_opportunity(
            idOportuninity=idSell,
            description=self.description,
            value=self.value,
            deadline=self.deadline,
            etapa=nullState(self.etapa),
            note=self.note,
            sourceOpportunity=self.sourceOpportunity,
            clientId=self.clientId,
            sellerId=self.sellerId
        )




