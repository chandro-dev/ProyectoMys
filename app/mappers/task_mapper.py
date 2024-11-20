from pydantic import BaseModel, Field
from datetime import datetime
from app.models.task_assignment_model import Task

class TaskSchema(BaseModel):
    title: str 
    description: str = Field(max_length=255)
    person_id: str
    creation_date: datetime
    end_date: datetime
    administration_id: int

    class Config:
        orm_mode = True
    def to_database_model(self) -> Task:
        return Task(
            title=self.title,
            description=self.description,
            person_id=self.person_id,
            creation_date=self.creation_date,
            end_date=self.end_date,
            administration_id=self.administration_id
        )