from fastapi import APIRouter, HTTPException
import random
from typing import List
from models.question import Pretest, PretestUpdate, Posttest, PosttestUpdate
from bson import ObjectId
from database.connection import pretest_collection, posttest_collection

router = APIRouter()

# PRE-TEST
@router.get("/pretest", response_model=List[Pretest])
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


@router.get("/question/pretest", response_model=List[Pretest])
async def get_pretest():
    pretest_list = [] 
    for pretest in pretest_collection.find({}):
        pretest['_id'] = str(pretest['_id'])
        pretest['pretest_id'] = pretest.pop('_id')
        pretest_list.append(pretest)
    return pretest_list


@router.get("/question/pretest/{id}", response_model=Pretest)
async def get_user(id: str):
    object_id = ObjectId(id)
    pretest = pretest_collection.find_one({"_id": object_id})
    if pretest:
        pretest['_id'] = str(pretest['_id'])
        pretest['pretest_id'] = pretest.pop('_id')
        return pretest
    else:
        raise HTTPException(status_code=404, detail="Question not found")
    
# PUT
@router.put("/question/pretest/{pretest_id}")
async def update_pretest(pretest_id: str, updated_pretest_data: PretestUpdate):
    object_id = ObjectId(pretest_id)
    pretest_exist = pretest_collection.find_one({"_id": object_id})
    if pretest_exist:
        updated_pretest_dict = updated_pretest_data.dict(exclude_unset=True)
        if updated_pretest_dict.get('options') is not None:
            updated_pretest_dict['options'] = updated_pretest_data.options
        pretest_collection.update_one({"_id": object_id}, {"$set": updated_pretest_dict})
        return {"message": "Pretest updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Pretest not found")
    
# POST-TEST
@router.get("/posttest", response_model=List[Posttest])
async def get_posttest():
    posttest_questions = list(posttest_collection.find({}, {"_id": 0}))
    
    # Shuffle the questions
    random.shuffle(posttest_questions)
    
    # Randomize options and option_images for each question
    for question in posttest_questions:
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
    
    return posttest_questions


@router.get("/question/posttest", response_model=List[Posttest])
async def get_posttest():
    posttest_list = [] 
    for posttest in posttest_collection.find({}):
        posttest['_id'] = str(posttest['_id'])
        posttest['posttest_id'] = posttest.pop('_id')
        posttest_list.append(posttest)
    return posttest_list


@router.get("/question/posttest/{id}", response_model=Posttest)
async def get_user(id: str):
    object_id = ObjectId(id)
    posttest = posttest_collection.find_one({"_id": object_id})
    if posttest:
        posttest['_id'] = str(posttest['_id'])
        posttest['posttest_id'] = posttest.pop('_id')
        return posttest
    else:
        raise HTTPException(status_code=404, detail="Question not found")
    
# PUT
@router.put("/question/posttest/{posttest_id}")
async def update_posttest(posttest_id: str, updated_posttest_data: PosttestUpdate):
    object_id = ObjectId(posttest_id)
    posttest_exist = posttest_collection.find_one({"_id": object_id})
    if posttest_exist:
        updated_posttest_dict = updated_posttest_data.dict(exclude_unset=True)
        if updated_posttest_dict.get('options') is not None:
            updated_posttest_dict['options'] = updated_posttest_data.options
        posttest_collection.update_one({"_id": object_id}, {"$set": updated_posttest_dict})
        return {"message": "Posttest updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Posttest not found")
