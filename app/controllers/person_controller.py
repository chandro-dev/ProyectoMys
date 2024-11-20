from fastapi import APIRouter, HTTPException,Body, Path, Query
from app.mappers.clients_mapper import PersonSchema
from app.services.persons_service import save_person,update_person,get_all

router = APIRouter()

@router.post("/person", tags=['Personas'])
def add_person(person:PersonSchema = Body()):
    return save_person(person.to_database_model)

@router.put("/person/{id}", tags=['Personas'])
def update_person_Id(id:str=Path, person:PersonSchema = Body()):
    return update_person(id,person.to_database_model)

@router.get("/persons", tags=['Personas'])
def get_all_persons():
    return get_all()