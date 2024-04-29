from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from models.classroom import Classroom
from database.connection import classrooms_collection
from bson import ObjectId
from typing import List

router = APIRouter()

# POST
@router.post("/createClassroom")
async def create_classroom(classroom: Classroom):
    teacher_object_id = ObjectId(classroom.teacherObjectId)
    classroom_data = classroom.model_dump()
    classroom_data['teacherObjectId'] = teacher_object_id
    classrooms_collection.insert_one(classroom_data)
    return

# GET
@router.get("/getClassroom/{id}", response_model=Classroom)
async def get_classroom(id: str):
    classroom = classrooms_collection.find_one({"_id": ObjectId(id)})
    classroom['_id'] = str(classroom['_id'])  
    classroom['teacherObjectId'] = str(classroom['teacherObjectId'])  
    classroom['classroomId'] = classroom.pop('_id')  
    classroom['students'] = [str(student_id) for student_id in classroom['students']]
    return classroom

@router.get("/getClassrooms/{id}", response_model=List[Classroom])
async def get_classroom(id: str):
    classrooms = []
    object_id = ObjectId(id)
    for classroom in classrooms_collection.find({"teacherObjectId": object_id}):
        classroom['_id'] = str(classroom['_id'])  
        classroom['teacherObjectId'] = str(classroom['teacherObjectId'])  
        classroom['classroomId'] = classroom.pop('_id')  
        classroom['students'] = [str(student_id) for student_id in classroom['students']]
        classrooms.append(classroom)
    return classrooms
    
# POST
@router.post("/updateClassroomStudentList/{id}")
async def add_students_to_classroom(id: str, student_ids: List[str]):
    object_id = ObjectId(id)
    classroom_exist = classrooms_collection.find_one({"_id": object_id})
    if classroom_exist:
        student_object_ids = [ObjectId(student_id) for student_id in student_ids]
        classrooms_collection.update_one({"_id": object_id}, {"$push": {"students": {"$each": student_object_ids}}})
        return {"message": "Students added to the classroom successfully"}
    else:
        raise HTTPException(status_code=404, detail="Classroom not found")
