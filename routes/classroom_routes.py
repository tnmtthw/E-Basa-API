from pymongo import MongoClient
from fastapi import APIRouter
from models.classroom import Classroom
from database.connection import classrooms_collection
from bson import ObjectId
from typing import List

router = APIRouter()

# POST
@router.post("/createClassroom")
def create_classroom(classroom: Classroom):
    teacher_object_id = ObjectId(classroom.teacherObjectId)
    classroom_data = classroom.model_dump()
    classroom_data['teacherObjectId'] = teacher_object_id
    classrooms_collection.insert_one(classroom_data)
    return

@router.get("/getClassrooms/{id}", response_model=List[Classroom])
def get_classroom(id: str):
    classrooms = []
    object_id = ObjectId(id)
    for classroom in classrooms_collection.find({"teacherObjectId": object_id}):
        classroom['teacherObjectId'] = str(classroom['teacherObjectId'])
        classroom['_id'] = str(classroom['_id'])
        classroom['classroomId'] = classroom.pop('_id')
        classrooms.append(classroom)
    return classrooms
