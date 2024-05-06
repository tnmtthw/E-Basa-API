from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from models.instruction import PretestInstruction, UpdatePretestInstruction, PosttestInstruction, UpdatePosttestInstruction
from database.connection import instruction_pre_collection, instruction_post_collection
from typing import List

router = APIRouter()

#PRE-TEST
# POST
@router.post("/pretestInstruction/")
def create_pretest_instruction(instruction: PretestInstruction):
    instruction_data = instruction.dict()
    instruction_pre_collection.insert_one(instruction_data)
    return {"Success"}

#GET
@router.get("/getPretestInstruction", response_model=List[PretestInstruction])
async def get_pretest_instruction_list():
    instructions = []
    for instruction in instruction_pre_collection.find({}):
        instructions.append(instruction)
    return instructions

@router.get("/getPretestInstruction/{instructionId}", response_model=PretestInstruction)
async def get_pretest_instruction(instructionId: str):
    instruction = instruction_pre_collection.find_one({"instructionId": instructionId})
    if instruction:
        return PretestInstruction(**instruction)
    else:
        raise HTTPException(status_code=404, detail="Instruction not found")
    
@router.put("/updatePretestInstruction/{instructionId}", response_model=UpdatePretestInstruction)
async def update_pretest_instruction(instructionId: str, updated_instruction: UpdatePretestInstruction):
    existing_instruction = instruction_pre_collection.find_one({"instructionId": instructionId})
    if existing_instruction:
        instruction_pre_collection.update_one({"instructionId": instructionId}, {"$set": updated_instruction.dict()})
        return updated_instruction
    else:
        raise HTTPException(status_code=404, detail="Instruction not found")
    
#POST-TEST   
# POST
@router.post("/posttestInstruction/")
def create_posttest_instruction(instruction: PosttestInstruction):
    instruction_data = instruction.dict()
    instruction_post_collection.insert_one(instruction_data)
    return {"Success"}

#GET
@router.get("/getPosttestInstruction", response_model=List[PosttestInstruction])
async def get_posttest_instruction_list():
    instructions = []
    for instruction in instruction_post_collection.find({}):
        instructions.append(instruction)
    return instructions

@router.get("/getPosttestInstruction/{instructionId}", response_model=PosttestInstruction)
async def get_posttest_instruction(instructionId: str):
    instruction = instruction_post_collection.find_one({"instructionId": instructionId})
    if instruction:
        return PosttestInstruction(**instruction)
    else:
        raise HTTPException(status_code=404, detail="Instruction not found")
    
@router.put("/updatePosttestInstruction/{instructionId}", response_model=UpdatePosttestInstruction)
async def update_posttest_instruction(instructionId: str, updated_instruction: UpdatePosttestInstruction):
    existing_instruction = instruction_post_collection.find_one({"instructionId": instructionId})
    if existing_instruction:
        instruction_post_collection.update_one({"instructionId": instructionId}, {"$set": updated_instruction.dict()})
        return updated_instruction
    else:
        raise HTTPException(status_code=404, detail="Instruction not found")