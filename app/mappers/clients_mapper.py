from pydantic import BaseModel, Field
from typing import Optional
from app.services.generations_service import id_generation
from app.models.persons_models import Person
from app.models.clients_Models import Clients
class PersonSchema(BaseModel):
    name: str = Field(max_length=255)
    secondName: int = Field(..., description="El campo valor es obligatorio")
    lastname: Optional[int] = None
    secondLastName: Optional[str] = None
    email: Optional[str] = None
    numberPhone: Optional[str] = None
    company: Optional[str] = None

    class Config:
        orm_mode = True
    def to_database_model(self) -> Person:
        idPerson=id_generation()
        return Person(
            id=idPerson,
            name=self.name,
            secondName=self.secondName,
            lastname=self.lastname,
            secondLastName=self.secondLastName,
            email=self.email,
            numberPhone=self.numberPhone
        )
    
    def to_client_model(self,person:Person) -> Clients:
        idClient = id_generation()
        return Clients(
            client_id= idClient,
            user_id = person.id,
            bussiness = self.company
        )
    
    
    
