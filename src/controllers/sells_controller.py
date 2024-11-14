from fastapi import APIRouter, HTTPException,Body, Path, Query
from src.services.sell_service import save_sales_opportunity, get_sales_opportunities_by_stage,get_all_sales_opportunities,delete_sales_opportunity,update_sales_opportunity_status
from src.mappers.sells_mapper import SalesOpportunitySchema

router = APIRouter()

@router.post("/sales", tags=['Oportunidades de ventas'])
def save_sell(sell:SalesOpportunitySchema = Body()):
    return save_sales_opportunity(sell.to_database_model())

@router.get("/getSales/{stage}",tags=['Oportunidades de ventas'])
def getSalesOportunity(stage:int=Path):
    return get_sales_opportunities_by_stage(stage)
