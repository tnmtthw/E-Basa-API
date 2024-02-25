from fastapi import APIRouter, HTTPException
from typing import List
from models.hugis import Hugis  # Corrected import
from database.connection import hugis_collection

router = APIRouter()

@router.get("/hugis", response_model=List[Hugis])
async def get_hugis():
    try:
        hugis = list(hugis_collection.find({}, {"_id": 0}))
        return hugis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
