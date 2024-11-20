from fastapi import APIRouter, HTTPException,Body, Path, Query
from app.services.sell_service import save_sales_opportunity, get_sales_opportunities_by_stage,get_all_sales_opportunities,delete_sales_opportunity,update_sales_opportunity_status
from app.mappers.sells_mapper import SalesOpportunitySchema

router = APIRouter()

@router.post("/sales", tags=['Oportunidades de ventas'])
def save_sell(sell:SalesOpportunitySchema = Body()):
    return save_sales_opportunity(sell.to_database_model())

@router.get("/getSales/{stage}",tags=['Oportunidades de ventas'])
def getSalesOportunity(stage:int=Path):
    return get_sales_opportunities_by_stage(stage)

@router.get("/getAll",tags=['Oportunidades de ventas'])
def getAllsalesOportunity():
    return get_all_sales_opportunities()

@router.delete("/deleteOportunity/{id}",tags=['Oportunidades de ventas'])
def deleteSalesOportunity(id:str=Path):
    return delete_sales_opportunity(id)

@router.put("/updateStatus/{idOportunity}/{status}",tags=['Oportunidades de ventas'])
def updateStatus(idOportunity:str=Path,status:str=Path):
    return update_sales_opportunity_status(idOportunity,status)