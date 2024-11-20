from fastapi import APIRouter, HTTPException,Body, Path
from app.mappers.task_mapper import TaskSchema
from app.services.Task_Service import create_task,update_task,delete_task,get_all_tasks,get_tasks_by_person_id
router = APIRouter()

@router.post("/task", tags=['Asignacion de tareas'])
def save_task(task:TaskSchema = Body()):
    return create_task(task.to_database_model())

@router.get("/getTask/{person}",tags=['Asignacion de tareas'])
def getTask(person:str=Path):
    return get_tasks_by_person_id(person)

@router.get("/getAllTask",tags=['Asignacion de tareas'])
def getAllTask():
    return get_all_tasks()

@router.delete("/deleteTask/{id}",tags=['Asignacion de tareas'])
def deleteTask(id:int=Path):
    return delete_task(id)

@router.put("/updateTask/{idOportunity}",tags=['Asignacion de tareas'])
def updateTask(idOportunity:int=Path,tarea:TaskSchema=Body()):
    return update_task(idOportunity,tarea.to_database_model)