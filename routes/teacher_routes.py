from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from models.teacher import Teacher
from database.connection import teachers_collection, authenticate_user
from typing import List

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# POST
@router.post("/createTeacherAccount")
def register_post(user: Teacher):
    user_exist = teachers_collection.find_one({"username": user.username})
    if user_exist:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    user_data = user.model_dump()
    teachers_collection.insert_one(user_data)
    return {"username": user.username, "userType": user.userType}

#GET
@router.get("/getTeacherAccount", response_model=List[Teacher])
async def get_users():
    users = []
    for user in teachers_collection.find({}):
        user['_id'] = str(user['_id'])
        user['teacherObjectId'] = user.pop('_id')
        users.append(user)
    return users
