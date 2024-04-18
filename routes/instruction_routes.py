from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from models.instruction import PretestInstruction, UpdatePretestInstruction
from database.connection import instruction_collection
from typing import List

router = APIRouter()

# POST
@router.post("/pretestInstruction/")
def create_pretest_instruction(instruction: PretestInstruction):
    instruction_data = instruction.dict()
    instruction_collection.insert_one(instruction_data)
    return {"Success"}

#GET
@router.get("/getPretestInstruction", response_model=List[PretestInstruction])
async def get_pretest_instruction_list():
    instructions = []
    for instruction in instruction_collection.find({}):
        instructions.append(instruction)
    return instructions

@router.get("/getPretestInstruction/{instructionId}", response_model=PretestInstruction)
async def get_pretest_instruction(instructionId: str):
    instruction = instruction_collection.find_one({"instructionId": instructionId})
    if instruction:
        return PretestInstruction(**instruction)
    else:
        raise HTTPException(status_code=404, detail="Instruction not found")
    
@router.put("/updatePretestInstruction/{instructionId}", response_model=UpdatePretestInstruction)
async def update_pretest_instruction(instructionId: str, updated_instruction: UpdatePretestInstruction):
    existing_instruction = instruction_collection.find_one({"instructionId": instructionId})
    if existing_instruction:
        instruction_collection.update_one({"instructionId": instructionId}, {"$set": updated_instruction.dict()})
        return updated_instruction
    else:
        raise HTTPException(status_code=404, detail="Instruction not found")