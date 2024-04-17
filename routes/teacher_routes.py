from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from models.teacher import Teacher, LoginRequest
from database.connection import teachers_collection, authenticate_teacher
from typing import List
from bson import ObjectId

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# POST
@router.post("/createTeacherAccount")
def register__teacher_post(user: Teacher):
    user_exist = teachers_collection.find_one({"username": user.username})
    if user_exist:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    user_data = user.model_dump()
    teachers_collection.insert_one(user_data)
    return {"username": user.username, "userType": user.userType}

@router.post("/loginTeacherAccount")
def login_teacher_post(login_data: LoginRequest):
    teacher = authenticate_teacher(login_data.username, login_data.password)
    if not teacher:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    teacherObjectId_value = str(teacher.get("_id"))

    return {"accessToken": teacher['username'], "firstName:": teacher['firstName'], "middleName": teacher['middleName'], "lastName": teacher['lastName'], "teacherObjectId": teacherObjectId_value}

#GET
@router.get("/getTeacherAccount", response_model=List[Teacher])
async def get_teacher_list():
    users = []
    for user in teachers_collection.find({}):
        user['_id'] = str(user['_id'])
        user['teacherObjectId'] = user.pop('_id')
        users.append(user)
    return users

@router.get("/getTeacherAccount/{id}", response_model=List[Teacher])
async def get_teacher():
    users = []
    for user in teachers_collection.find({}):
        user['_id'] = str(user['_id'])
        user['teacherObjectId'] = user.pop('_id')
        users.append(user)
    return users

@router.delete("/deleteTeacherAccount/{teacherObjectId}")
async def delete_teacher(teacherObjectId: str):
    object_id = ObjectId(teacherObjectId)
    deletion_result = teachers_collection.delete_one({"_id": object_id})
    if deletion_result.deleted_count == 1:
        return {"message": "Teacher account deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Teacher account not found")


