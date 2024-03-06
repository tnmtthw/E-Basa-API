from fastapi import APIRouter
import random
from typing import List
from models.question import PreTest
from database.connection import pretest_collection

router = APIRouter()

@router.get("/pretest", response_model=List[PreTest])
async def get_pretest():
    pretest_questions = list(pretest_collection.find({}, {"_id": 0}))
    
    # Shuffle the questions
    random.shuffle(pretest_questions)
    
    # Randomize options and option_images for each question
    for question in pretest_questions:
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
    
    return pretest_questions
