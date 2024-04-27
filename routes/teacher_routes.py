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
    return {"accessToken": teacher['username'], "avatar": teacher['avatar'], "firstName": teacher['firstName'], "middleName": teacher['middleName'], "lastName": teacher['lastName'], "teacherObjectId": teacherObjectId_value}

#GET
@router.get("/getTeacherAccount", response_model=List[Teacher])
async def get_teacher_list():
    teachers = []
    for teacher in teachers_collection.find({}):
        teacher['_id'] = str(teacher['_id'])
        teacher['teacherObjectId'] = teacher.pop('_id')
        teachers.append(teacher)
    return teachers


@router.get("/getTeacherAccount/{id}", response_model=Teacher)
async def get_teacher(id: str):
    object_id = ObjectId(id)
    teacher = teachers_collection.find_one({"_id": object_id})
    if teacher:
        teacher['_id'] = str(teacher['_id'])
        teacher['teacherObjectId'] = teacher.pop('_id')
        return teacher
    else:
        raise HTTPException(status_code=404, detail="Teacher account not found")

@router.delete("/deleteTeacherAccount/{teacherObjectId}")
async def delete_teacher(teacherObjectId: str):
    object_id = ObjectId(teacherObjectId)
    deletion_result = teachers_collection.delete_one({"_id": object_id})
    if deletion_result.deleted_count == 1:
        return {"message": "Teacher account deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Teacher account not found")
    
# PUT
@router.put("/getTeacherAccount/{teacherObjectId}")
async def update_teacher(teacherObjectId: str, updated_user_data: Teacher):
    object_id = ObjectId(teacherObjectId)
    user_exist = teachers_collection.find_one({"_id": object_id})
    if user_exist:
        updated_user_dict = updated_user_data.model_dump(exclude_unset=True)
        teachers_collection.update_one({"_id": object_id}, {"$set": updated_user_dict})
        return {"message": "Teacher updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")


