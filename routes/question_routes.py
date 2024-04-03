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

@router.get("/question/pretest", response_model=List[PreTest])
async def get_pretest():
    pretest_questions = list(pretest_collection.find({}, {"_id": 0}))
    return pretest_questions

from typing import Optional

@router.put("/question/pretest/{question_id}", response_model=PreTest)
async def update_pretest_question(question_id: str, updated_fields: dict):
    # Convert question_id to ObjectId
    object_id = ObjectId(question_id)
    
    # Check if the question exists in the collection
    question_exist = pretest_collection.find_one({"_id": object_id})
    
    if question_exist:
        # Formulate update query based on provided fields
        update_query = {"$set": {}}
        for field, value in updated_fields.items():
            update_query["$set"][field] = value

        # Update the question in the database with the provided question_id
        result = pretest_collection.update_one({"_id": object_id}, update_query)
        
        if result.modified_count == 1:
            # Retrieve the updated question with the actual _id
            updated_question = pretest_collection.find_one({"_id": object_id})
            return updated_question
        else:
            raise HTTPException(status_code=500, detail="Failed to update question")
    else:
        raise HTTPException(status_code=404, detail="Question not found")
