from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from models.instruction import PretestInstruction
from database.connection import instruction_collection

router = APIRouter()

# POST
@router.post("/pretestInstruction/")
def create_pretest_instruction(instruction: PretestInstruction):
    instruction_data = instruction.dict()
    instruction_collection.insert_one(instruction_data)
    return {"Success"}
