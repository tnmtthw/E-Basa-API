from fastapi import APIRouter, HTTPException
import random
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
    
    # Shuffle the questions
    random.shuffle(kulay)
    
    # Randomize options and option_images for each question
    for question in kulay:
        options = question["options"]
        option_images = question["option_images"]
        correct_index = question["correct_option_index"]
        
        # Ensure correct option index is within the first 4 options
        if correct_index >= 4:
            options = options[:3] + [options[correct_index]]
            option_images = option_images[:3] + [option_images[correct_index]]
            correct_index = 3
        
        # Construct list of indices for options and option_images
        indices = list(range(len(options)))
        
        # Shuffle the indices
        random.shuffle(indices)
        
        # If correct index is not within the first 4 options, place it randomly within them
        if correct_index not in indices[:4]:
            replace_index = random.randint(0, 3)
            indices[replace_index] = correct_index
        
        # Update correct option index
        question["correct_option_index"] = indices.index(correct_index)
        
        # Update question with shuffled options and option_images
        question["options"] = [options[i] for i in indices[:4]]
        question["option_images"] = [option_images[i] for i in indices[:4]]
    
    return kulay

# @router.get("/kulay", response_model=List[Kulay])
# async def get_kulay():
#     kulay = list(kulay_collection.find({}, {"_id": 0}))
#     return kulay

@router.get("/numero", response_model=List[Numero])
async def get_numero():
    numero = list(numero_collection.find({}, {"_id": 0}))
    return numero