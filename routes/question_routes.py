from fastapi import APIRouter, HTTPException
from typing import List
from models.question import Hugis, Kulay, Numero, Binasa, Napakinggan, Ponolohiya, Talasalitaan, Gramatika
from database.connection import hugis_collection, kulay_collection, numero_collection, binasa_collection, napakinggan_collection, ponolohiya_collection, talasalitaan__collection, gramatika__collection

router = APIRouter()

@router.get("/hugis", response_model=List[Hugis])
async def get_hugis():
    hugis = list(hugis_collection.find({}, {"_id": 0}))
    return hugis

@router.get("/kulay", response_model=List[Kulay])
async def get_kulay():
    kulay = list(kulay_collection.find({}, {"_id": 0}))
    return kulay

@router.get("/numero", response_model=List[Numero])
async def get_numero():
    numero = list(numero_collection.find({}, {"_id": 0}))
    return numero

@router.get("/binasa", response_model=List[Binasa])
async def get_binasa():
    binasa = list(binasa_collection.find({}, {"_id": 0})) 
    return binasa

@router.get("/napakinggan", response_model=List[Napakinggan]) 
async def get_napakinggan():
    napakinggan = list(napakinggan_collection.find({}, {"_id": 0})) 
    return napakinggan

@router.get("/ponolohiya", response_model=List[Ponolohiya]) 
async def get_ponolohiya():
    ponolohiya = list(ponolohiya_collection.find({}, {"_id": 0})) 
    return ponolohiya

@router.get("/talasalitaan", response_model=List[Talasalitaan]) 
async def get_talasalitaan():
    talasalitaan = list(talasalitaan__collection.find({}, {"_id": 0})) 
    return talasalitaan

@router.get("/gramatika", response_model=List[Gramatika]) 
async def get_gramatika():
    gramatika = list(gramatika__collection.find({}, {"_id": 0})) 
    return gramatika




