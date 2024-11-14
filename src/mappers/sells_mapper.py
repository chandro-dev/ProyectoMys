from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from src.models.sales_opportunity import Sales_opportunity
class SalesOpportunitySchema(BaseModel):
    idOportuninity: str
    description: str
    value: int
    deadline: datetime
    etapa: Optional[int] = None
    note: Optional[str] = None
    sourceOpportunity: Optional[str] = None
    clientId: Optional[str] = None
    sellerId: Optional[str] = None

    class Config:
        orm_mode = True
    def to_database_model(self) -> Sales_opportunity:
        return Sales_opportunity(
            idOportuninity=self.idOportuninity,
            description=self.description,
            value=self.value,
            deadline=self.deadline,
            etapa=self.etapa,
            note=self.note,
            sourceOpportunity=self.sourceOpportunity,
            clientId=self.clientId,
            sellerId=self.sellerId
        )




